import os
import csv
import json


BUILDER_CSV_FIELD_NAMES = [
    'record',
    'tag_number', 'tag_v3', 'tag_vn', 'field_name',
    'subfield', 'subfield_name',
    'format', 'parent', 'name',
]


class ModelBuilder:

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
            tag = row["tag_v3"]
            recs[rec_type] = recs.get(rec_type) or {}
            recs[rec_type][tag] = recs[rec_type].get(tag) or {}
            if not recs[rec_type][tag]:
                recs[rec_type][tag] = {
                    l: row[l]
                    for l in ["tag_number", "tag_v3", "tag_vn",
                              "field_name", "format"]
                }
                recs[rec_type][tag]["subfields"] = {}

            if row["subfield"]:
                recs[rec_type][tag]["subfields"].update(
                    {row["subfield"]: row["subfield_name"]}
                )
        self._grouped_by_rec_and_tag = recs

    @property
    def templates(self):
        if not self._grouped_by_rec_and_tag:
            self._group_by_rec_and_tag()
        return self._grouped_by_rec_and_tag

    def generate_class_file(self, output_file_path):
        with open(output_file_path, "w") as fp:
            fp.write("from scielo_idb.id_records import IdRecord\n\n")

        for rec_type, tags in self.templates.items():
            class_name = f"RecordType{rec_type.upper()}"

            blocks = [
                _class_init_builder(class_name),
            ]
            for tag in tags.keys():
                blocks.append(
                    _attribute_builder(tags[tag]['field_name'], tag))

            with open(output_file_path, "a") as fp:
                fp.write("\n".join(blocks))
                fp.write("\n"*2)


def _class_init_builder(class_name):
    return "\n".join((
        f"""""",
        f"""class {class_name}(IdRecord):""",
        f"""""",
        f"""    def __init__(self, record, data_dictionary):""",
        f"""        super().__init__(record, data_dictionary)""",
    ))


def _attribute_builder(attribute_name, tag):
    return "\n".join((
        f"""""",
        f"""    @property""",
        f"""    def {attribute_name}(self):""",
        f"""        return self.get_data('{tag}')""",
    ))
