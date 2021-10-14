import argparse
import os
import csv
import json


BUILDER_CSV_FIELD_NAMES = [
    'record',
    'tag', 'subfield', 'subfield_name',
    'no_repetition', 'no_subfield',
    'field_name',
    'name', 'description',
]


class DataDictionaryBuilder:

    def __init__(self, file_path):
        self._file_path = file_path
        self._grouped_by_rec_and_tag = None

    def _read(self):
        with open(self._file_path, newline='') as csvfile:
            reader = csv.DictReader(
                csvfile, delimiter=',', fieldnames=BUILDER_CSV_FIELD_NAMES)
            for row in reader:
                yield row

    def _group_by_rec_and_tag(self):
        recs = {}
        for row in self._read():
            rec_type = row["record"]
            tag_number = row["tag"]
            tag = "v" + tag_number.zfill(3)
            recs[rec_type] = recs.get(rec_type) or {}
            recs[rec_type][tag] = recs[rec_type].get(tag) or {}
            if not recs[rec_type][tag]:
                for l in ("field_name", "no_repetition", "no_subfield"):
                    recs[rec_type][tag][l] = row.get(l) or ""
                recs[rec_type][tag]["subfields"] = {}
            if row["subfield"]:
                recs[rec_type][tag]["subfields"].update(
                    {row["subfield"]: row["subfield_name"]}
                )
        self._grouped_by_rec_and_tag = recs

    @property
    def data_dictionary(self):
        if not self._grouped_by_rec_and_tag:
            self._group_by_rec_and_tag()
        return self._grouped_by_rec_and_tag or {}

    def get_record_data_dictionary(self, rec_type):
        if not self._grouped_by_rec_and_tag:
            self._group_by_rec_and_tag()
        return self._grouped_by_rec_and_tag.get(rec_type) or {}

    def save(self, output_json_file_path):
        with open(output_json_file_path, "w") as fp:
            fp.write(json.dumps(self.data_dictionary, indent=2))


class ModelBuilder:

    def __init__(self, class_name, data_dictionary):
        self._class_name = class_name
        self._data_dictionary = data_dictionary

    def create_module(self, class_file_path):
        with open(class_file_path, "w") as fp:
            fp.write("from iid2json.meta_record import MetaRecord\n\n")

    def add_class(self, class_file_path):
        blocks = [
            _class_init_builder(f"{self._class_name}"),
        ]
        for tag, tag_info in self._data_dictionary.items():
            subfields = tag_info.get('subfields') or {}
            if subfields:
                if len(subfields) == 1 and "_" in subfields.keys() and not subfields["_"]:
                    tag_info["subfields"] = None

            field_name = tag_info.get('field_name') or tag
            subfields = tag_info.get('subfields') or {}
            no_repetition = tag_info.get('no_repetition') or ''
            no_subfield = tag_info.get('no_subfield') or ''

            comment = _get_comment(tag, tag_info)
            blocks.append(
                _attribute_builder(
                    field_name, tag, subfields, no_repetition, no_subfield,
                    comment,
                )
            )

        with open(class_file_path, "a") as fp:
            fp.write("\n".join(blocks))
            fp.write("\n"*2)


def _get_comment(tag, tag_info):
    field_name = tag_info.get('field_name') or tag
    subfields = tag_info.get('subfields') or ''
    no_repetition = tag_info.get('no_repetition') or ''
    no_subfield = tag_info.get('no_subfield') or ''
    name = tag_info.get('name') or field_name
    description = tag_info.get('description') or name
    rows = [
        '',
        '"""',
        f"{description}",
        "",
        f"{tag} {subfields}",
        '"""',
    ]
    comment_rows = []
    for row in rows[1:]:
        comment_rows.append(" "*8 + row.strip() if row else '')
    return "\n".join(comment_rows)


def _class_init_builder(class_name):
    return "\n".join((
        f"""""",
        f"""class {class_name}(MetaRecord):""",
        f"""""",
        f"""    def __init__(""",
        f"""            self, record, no_repetition_tags=None, no_subfield_tags=None,""",
        f"""            data_dictionary=None):""",
        f"""        super().__init__(""",
        f"""            record, no_repetition_tags, no_subfield_tags, data_dictionary)""",
    ))


def _attribute_builder(attribute_name, tag, subfields, no_repetition, no_subfield, comment=""):
    format_before_tag = ""
    virg_and_new_line = ",\n" + " "*12

    optional_params = {}
    if subfields:
        optional_params["subfields"] = subfields
    if no_repetition:
        optional_params["no_repetition"] = True
    if no_subfield:
        optional_params["no_subfield"] = True

    params = [f'"{tag}"']
    if optional_params:
        params.extend(
            [f"{name}={value}" for name, value in optional_params.items()])
        format_before_tag = "\n" + " "*12
    params = virg_and_new_line.join(params)

    return "\n".join((
        f"""""",
        f"""    @property""",
        f"""    def {attribute_name}(self):""",
        f"""{comment}""",
        f"""        return self.get_field_content({format_before_tag}{params})""",
    ))


def main():
    parser = argparse.ArgumentParser(
        description="Data Dictionary tool")
    subparsers = parser.add_subparsers(
        title="Commands", metavar="", dest="command")

    generate_json_data_dictionary_parser = subparsers.add_parser(
        "generate_json_data_dictionary",
        help=(
            "Generate data dicionary json file"
        )
    )
    generate_json_data_dictionary_parser.add_argument(
        "data_dictionary_csv_file_path",
        help=(
            "data dictionary csv file path"
        )
    )

    generate_json_data_dictionary_parser.add_argument(
        "data_dictionary_json_file_path",
        help=(
            "data dictionary json file path"
        )
    )

    generate_module_parser = subparsers.add_parser(
        "generate_module_py",
        help=(
            "Generate python module"
        )
    )

    generate_module_parser.add_argument(
        "data_dictionary_json_file_path",
        help=(
            "data_dictionary json file path"
        )
    )

    generate_module_parser.add_argument(
        "record_type",
        help=(
            "output file"
        )
    )

    generate_module_parser.add_argument(
        "class_name",
        help=(
            "output file"
        )
    )

    generate_module_parser.add_argument(
        "class_file_path",
        help=(
            "output file"
        )
    )

    args = parser.parse_args()
    if args.command == "generate_json_data_dictionary":
        builder = DataDictionaryBuilder(args.data_dictionary_csv_file_path)
        builder.save(args.data_dictionary_json_file_path)
    elif args.command == "generate_module_py":
        with open(args.data_dictionary_json_file_path) as fp:
            data_dict = json.loads(fp.read())
        builder = ModelBuilder(args.class_name, data_dict[args.record_type])
        builder.create_module(args.class_file_path)
        builder.add_class(args.class_file_path)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
