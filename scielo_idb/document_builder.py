import argparse

from scielo_idb.id2json import (
    get_id_file_rows,
    join_id_file_rows_and_return_records,
    get_id_and_json_records,
    article_id,
)

from scielo_idb.data_dictionary import ModelBuilder
from scielo_idb.meta_record import MetaRecord, build_object


class MetaDocument:

    def __init__(self, _id, _records, data_dictionary):
        self._id = _id
        self._records = _records
        self._meta_records = None
        self._data_dictionary = data_dictionary

    @property
    def meta_records(self):
        if not self._meta_records:
            self._meta_records = {}
            for rec in self._records:
                meta_record = MetaRecord(rec)
                if not meta_record.rec_type:
                    continue
                rec_type = meta_record.rec_type
                self._meta_records[rec_type] = (
                    self._meta_records.get(rec_type) or []
                )
                self._meta_records[rec_type].append(meta_record)
        return self._meta_records

    def get_meta_records(self, rec_type):
        return self.meta_records.get(rec_type) or []

    def get_records_as_dict(self, rec_type, data_dict={}):
        return [
            _meta_rec.get_record_as_dict(data_dict)
            for _meta_rec in self.get_meta_records(rec_type)
        ]

    def get_records_as_object(self, rec_type, data_dict):
        for _meta_rec in self.get_meta_records(rec_type):
            _rec_as_dict = _meta_rec.get_record_as_dict(data_dict)
            build_object(_meta_rec, _rec_as_dict)
            yield _meta_rec


def get_documents(id_file_path, data_dictionary):
    rows = get_id_file_rows(id_file_path)
    records_content = join_id_file_rows_and_return_records(rows)
    for _id, _records in get_id_and_json_records(records_content, article_id):
        yield MetaDocument(_id, _records, data_dictionary)


def main():
    parser = argparse.ArgumentParser(
        description="Document tool")
    subparsers = parser.add_subparsers(
        title="Commands", metavar="", dest="command")

    get_documents_parser = subparsers.add_parser(
        "get_documents",
        help=(
            "Generate document model json"
        )
    )
    get_documents_parser.add_argument(
        "id_file_path",
        help=(
            "path of id_file_path"
        )
    )
    get_documents_parser.add_argument(
        "doc_csv_path",
        help=(
            "path of id_file_path"
        )
    )

    args = parser.parse_args()
    if args.command == "get_documents":
        model_builder = ModelBuilder(args.doc_csv_path)

        for doc in get_documents(args.id_file_path, model_builder.templates):
            for rec in doc.get_records_as_dict("c") or []:
                print("result", rec)
            for rec in doc.get_records_as_object(
                    "c", model_builder.templates.get("c")) or []:
                print("result", rec)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
