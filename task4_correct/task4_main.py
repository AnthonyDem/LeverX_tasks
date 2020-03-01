import argparse
import LoadData as ld
import ConversionData as cd
import Exceptions as ex
import sql_queries
import sql_functions


def query_name(select_num):
    queries = {
        '0': 'room_list_with_students_inside',
        '1': 'top5_avg_age',
        '2': 'top5_max_age_diff',
        '3': 'sex_diff'
    }
    for i in queries:
        if select_num == int(i):
            return queries.get(i)


def main(students_file, rooms_file, out_format):
    loader = ld.LoadJSON()
    students = loader.load(filename=students_file)
    rooms = loader.load(filename=rooms_file)
    db = sql_functions.DBops()

    db.create_table()

    for query in sql_queries.INDEX_QUERY:
        db.select_query(query)

    db.insert_queries(rooms, students)

    db.commit()

    for select_num, query in enumerate(sql_queries.SELECT_QUERIES):
        result = db.select_query(query)
        try:
            if out_format.lower() == 'json':
                conversion_json = cd.JSONConversion()
                conversion_json.write(result, 'select_' + query_name(select_num) + out_format)
            elif out_format.lower() == "xml":
                conversion_xml = cd.XMLConversion()
                conversion_xml.write(result, 'select_' + query_name(select_num) + out_format)
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
