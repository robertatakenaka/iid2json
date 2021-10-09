import argparse
from scielo_idb.models.tools.converter_data_dictionary import generate_csv


def main():
    parser = argparse.ArgumentParser(
        description="Data Dictionary tool")
    subparsers = parser.add_subparsers(
        title="Commands", metavar="", dest="command")

    generate_converter_document_data_dict_parser = subparsers.add_parser(
        "generate_converter_document_data_dict",
        help=(
            "Generate document model json"
        )
    )
    generate_converter_document_data_dict_parser.add_argument(
        "article_2db_file_path",
        help=(
            "path of article.2db"
        )
    )

    generate_converter_document_data_dict_parser.add_argument(
        "article_trans_file_path",
        help=(
            "path of article.trl"
        )
    )

    generate_converter_document_data_dict_parser.add_argument(
        "artmodel_txt_file_path",
        help=(
            "path of artmodel.txt"
        )
    )

    generate_converter_document_data_dict_parser.add_argument(
        "document_model_csv_file_path",
        help=(
            "output file"
        )
    )

    generate_class_parser = subparsers.add_parser(
        "generate_class",
        help=(
            "Generate document model json"
        )
    )

    generate_class_parser.add_argument(
        "document_model_csv_file_path",
        help=(
            "document model csv file path"
        )
    )

    generate_class_parser.add_argument(
        "class_file_path",
        help=(
            "output file"
        )
    )

    args = parser.parse_args()
    if args.command == "generate_converter_document_data_dict":
        generate_csv(
            args.article_2db_file_path, args.artmodel_txt_file_path,
            args.article_trans_file_path,
            args.document_model_csv_file_path)
    elif args.command == "generate_class":
        model_builder = ModelBuilder(args.document_model_csv_file_path)
        model_builder.generate_class_file(args.class_file_path)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
