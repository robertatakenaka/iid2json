import argparse

from scielo_idb.id2json import (
    get_id_file_rows,
    join_id_file_rows_and_return_records,
    get_id_and_json_records,
    article_id,
)
from scielo_idb.record_types import RecordTypeC, RecordTypeF, IdRecord
from scielo_idb.data_dictionary import ModelBuilder

RECORD_TYPE_CLASSES = {
    "c": RecordTypeC,
    "f": RecordTypeF,
}


def get_class(rec_type):
    return RECORD_TYPE_CLASSES.get(rec_type) or IdRecord


class Document:

    def __init__(self, _id, _records, data_dictionary):
        self._id = _id
        self._records = {}
        for rec in _records:
            rec_type = self.get_rec_type(rec)
            if rec_type:
                self._records[rec_type] = self._records.get(rec_type) or []
                Class = get_class(rec_type)
                self._records[rec_type].append(Class(rec, data_dictionary))

    def get_rec_type(self, record):
        try:
            return record.get("v706")[0]["_"]
        except:
            return

    @property
    def o_record(self):
        return self._records.get("o")[0]

    @property
    def h_record(self):
        return self._records.get("h")[0]

    @property
    def c_records(self):
        return self._records.get("c")

    @property
    def p_records(self):
        return self._records.get("p")


def get_documents(id_file_path, data_dictionary):
    rows = get_id_file_rows(id_file_path)
    records_content = join_id_file_rows_and_return_records(rows)
    for _id, _records in get_id_and_json_records(records_content, article_id):
        yield Document(_id, _records, data_dictionary)


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
            for rec in doc.c_records or []:
                print("result", list(rec.analytic_author))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
