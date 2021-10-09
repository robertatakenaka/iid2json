import os
import argparse
import csv
import json

FROM_TO = (
    ("author", "author"),
    ("corpaut", "corpauth"),
    ("serial", "serial"),
    ("vancouv", "reference"),
    ("apa", "reference"),
    ("abnt", "reference"),
    ("iso690", "reference"),
    ("monog", "monograph"),
    ("contrib", "analytic"),
    ("thes", "thesis"),
    ("conf", "conference"),
    ("sertitle", "source"),
    ("stitle", "source"),
    ("volid", "volume"),
    ("issueno", "number"),
    ("supplvol", "suppl"),
    ("supplno", "suppl"),
    ("hist", "history"),
)


DOC_BUILDER_CSV_FIELD_NAMES = [
    'record', 'tag', 'field_name', 'subfield', 'subfield_name',
    'format', 'parent', 'name',
]


class DocumentModelBuilder:

    def __init__(self, file_path):
        self._file_path = file_path
        self._grouped_by_rec_and_tag = None

    def _read(self):
        with open(self._file_path, newline='') as csvfile:
            reader = csv.DictReader(
                csvfile, delimiter=',', fieldnames=DOC_BUILDER_CSV_FIELD_NAMES)
            for row in reader:
                yield row

    def _group_by_rec_and_tag(self):
        recs = {}
        for row in self._read():
            rec_type = row["record"]
            tag = row["tag"]
            recs[rec_type] = recs.get(rec_type) or {}
            recs[rec_type][tag] = recs[rec_type].get(tag) or {}
            if not recs[rec_type][tag]:
                recs[rec_type][tag]["field_name"] = row["field_name"]
                recs[rec_type][tag]["format"] = row["format"]
                recs[rec_type][tag]["subfields"] = {}

            if row["subfield"]:
                recs[rec_type][tag]["subfields"].update(
                    {row["subfield"]: row["subfield_name"]}
                )
        self._grouped_by_rec_and_tag = recs

    def get_record_template(self, record_type=None):
        if not self._grouped_by_rec_and_tag:
            self._grouped_by_rec_and_tag()
        if self._grouped_by_rec_and_tag:
            if record_type:
                return self._grouped_by_rec_and_tag.get(record_type)
            return self._grouped_by_rec_and_tag


def _apply_standard(word):
    for f, t in FROM_TO:
        if f in word:
            return t
    return word


def _get_parent(path):
    _path = path.split(",")[::-1]
    if "p" in _path:
        i = _path.index("p")
        return [_apply_standard(w) for w in _path[i+1:]]
    for param in ("citat", "abkey", "bibcom", "bab", "front", "back", "abkey",
                  "article", "text"):
        if param in path:
            for i, item in enumerate(_path):
                if param in item or param == item:
                    print(param, item, _path, path, [_apply_standard(w) for w in _path[i+1:]])
                    return [_apply_standard(w) for w in _path[i+1:]]
    return [_apply_standard(w) for w in _path]


def _read_article_2db(file_path):
    """
    converter - article.2db
    """
    done = set()
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            tag, name, path = row
            if name == "ign":
                continue
            if "citat" in path:
                rec = "c"
            else:
                rec = "f"
            parent = "_".join(_get_parent(path))
            values = tag, name, parent, rec
            if values not in done:
                done.add(values)
                yield {
                    "tag": tag, "name": name, "parent": parent, "record": rec}


def _read_article_trans(file_path):
    """
    converter - article.trl
    """
    translations = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            tag, name = row
            translations[tag] = name
    return translations


def _read_artmodel_txt(file_path):
    """
    ```console
    id2i artmodel.id create=artmodel
    echo "number|name|attr|name2|parent|parent2|parent_index|record|fields|field_index|retag|formato|process"  >artmodel.txt
    mx artmodel lw=9999 "pft=(if 'fc':v8^r and v8^p='1' and s(v8^s,v8^f)<>''  then v1[1],'|',v2[1],'|',v3[1],'|',v4[1],'|',v5[1],'|',v6[1],'|',v7[1],'|',v8^r,'|',replace(v8^c,'|','/'),'|',v8^i,'|',v8^f,'|',v8^s,'|',v8^h,'|',v8^p,/ fi)" now >> artmodel.txt
    ```
    """
    fieldnames = "number|name|attr|name2|parent|parent2|parent_index|record|fields|field_index|retag|subfield|format|process".split("|")
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|', fieldnames=fieldnames)
        for row in reader:
            yield row


def _as_dict(rows, key="number"):
    tags = {}
    for row in rows:
        k = row[key]
        tags.setdefault(k, [])
        tags[k].append(row)
    return tags


def _get_attribute_name(_names):
    return "_".join(
                [name for name in _names if name]
            ).replace("-", "_")


def _generate_csv(artmodel_items, article_2db_items, article_trans):
    artmodel_dict = _as_dict(artmodel_items)

    for article_2db_item in article_2db_items:
        print("")
        print("article_2db_item", article_2db_item)

        number = article_2db_item["tag"]
        template = article_trans.get(number)
        items = (
            template and artmodel_dict.get(template) or
            artmodel_dict.get(number)
        )
        new_item = {}
        new_item.update(article_2db_item)

        if not items:

            _names = [article_2db_item['parent'], article_2db_item['name']]
            new_item["tag"] = f"{number}"
            new_item["field_name"] = _get_attribute_name(_names)
            new_item["subfield"] = ""
            new_item["subfield_name"] = ""
            new_item["format"] = False

            print("xxx", article_2db_item, new_item)
            yield new_item

            continue

        for item in items:
            record_type = item["record"]
            if record_type != article_2db_item["record"]:
                # print("X-RECTYPE", item)
                continue

            item_name = _apply_standard(item["name"])
            if item_name and item_name != article_2db_item["name"]:
                # print("X-NAME", item)
                continue

            if item.get("subfield") and len(item.get("subfield")) != 1:
                continue

            tag = item.get('retag') or number
            if not tag:
                print("X-TAG", item)
                continue

            _names = [article_2db_item['parent']]
            if not item.get("subfield"):
                _names.append(article_2db_item['name'])
            new_item["tag"] = f"{tag}"
            new_item["field_name"] = _get_attribute_name(_names)
            new_item["subfield"] = item.get("subfield") or "_"
            new_item["subfield_name"] = _get_attribute_name([item_name])
            new_item["format"] = item["format"] == "1"
            print(new_item)
            yield new_item


def generate_csv(artmodel_items, article_2db_items, article_trans, file_path):
    # print(records)
    dirname = os.path.dirname(file_path)
    if dirname and not os.path.isdir(dirname):
        os.makedirs(dirname)

    g = _generate_csv(artmodel_items, article_2db_items, article_trans)
    items = {}
    for item in g:
        key = (item["record"], item["tag"], item["field_name"])
        items.setdefault(key, [])
        items[key].append(item)

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=DOC_BUILDER_CSV_FIELD_NAMES)

        writer.writeheader()
        for key in sorted(items.keys()):
            for item in items[key]:
                writer.writerow(item)


def main():
    parser = argparse.ArgumentParser(
        description="Data Dictionary tool")
    subparsers = parser.add_subparsers(
        title="Commands", metavar="", dest="command")

    get_document_model_as_csv_parser = subparsers.add_parser(
        "get_document_model_as_csv",
        help=(
            "Generate document model json"
        )
    )
    get_document_model_as_csv_parser.add_argument(
        "article_2db_file_path",
        help=(
            "path of article.2db"
        )
    )

    get_document_model_as_csv_parser.add_argument(
        "article_trans_file_path",
        help=(
            "path of article.trl"
        )
    )

    get_document_model_as_csv_parser.add_argument(
        "artmodel_txt_file_path",
        help=(
            "path of artmodel.txt"
        )
    )

    get_document_model_as_csv_parser.add_argument(
        "document_model_csv_file_path",
        help=(
            "output file"
        )
    )

    args = parser.parse_args()
    if args.command == "get_document_model_as_csv":
        article_2db_items = _read_article_2db(args.article_2db_file_path)
        artmodel_items = _read_artmodel_txt(args.artmodel_txt_file_path)
        article_trans_dict = _read_article_trans(args.article_trans_file_path)
        generate_csv(
            artmodel_items, article_2db_items, article_trans_dict,
            args.document_model_csv_file_path)
    elif args.command == "get_document_model":
        article_2db_items = _read_article_2db(args.article_2db_file_path)
        artmodel_items = _read_artmodel_txt(args.artmodel_txt_file_path)
        article_trans_dict = _read_article_trans(args.article_trans_file_path)
        _generate_json(
            artmodel_items, article_2db_items, article_trans_dict,
            args.document_model_json_file_path)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
