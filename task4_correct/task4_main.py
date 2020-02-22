import argparse
import LoadData as ld
import ConversionData as cd
import Exceptions as ex
import sql_queries
import sql_functions

loader = ld.LoadJSON()
conversion_json = cd.JSONConversion()
conversion_xml = cd.XMLConversion()
db = sql_functions.DBops()


def main(students_file, rooms_file, out_format):
    filename = 'output.' + out_format
    students = loader.load(filename=students_file)
    rooms = loader.load(filename=rooms_file)

    db.create_table()

    for query in sql_queries.Queries.create_queries():
        db.select_query(query)

    db.insert_queries(rooms, students)

    db.commit()

    for query in sql_queries.Queries.select_queries():
        result = db.select_query(query)
        try:
            if out_format.lower() == 'json':
                conversion_json.write(result, filename)
            elif out_format.lower() == "xml":
                conversion_xml.write(result, filename)
            else:
                raise ex.FormatException('Please enter format json or xml')
        except ex.FormatException as fe:
            print(fe)


def argparser():
    parser = argparse.ArgumentParser('Connect two JSON files and print '
                                     'them in the format JSON or XML')
    parser.add_argument('path_to_students_file', type=str,
                        help='enter path to students file ')
    parser.add_argument('path_to_rooms_file', type=str,
                        help='enter path to rooms file ')
    parser.add_argument('output_format', type=str,
                        help='enter output format ')

    return parser


if __name__ == '__main__':
    parser = argparser()
    args = parser.parse_args()
    main(args.path_to_students_file, args.path_to_rooms_file, args.output_format)
