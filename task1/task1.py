import argparse
import LoadData as ld
import ConversionData as cd
import Exceptions as ex

loader = ld.LoadJSON()
conversion_json = cd.JSONConversion()
conversion_xml = cd.XMLConversion()


def related_json_data(students, rooms):
    rooms_with_students= {room["id"]:{'name':room['name'], 'students':[]} for room in rooms}
    related_data = []
    for student in students:
        students_in_room=rooms_with_students.get(student.get('room'))
        students_in_room.get('students').append(student)
    for room in rooms_with_students.items():
        related_data.append({'id': room[0], **room[1]})
    return related_data


def main(students_file, rooms_file, out_format):
    filename = 'output.' + out_format
    students = loader.load(filename=students_file)
    rooms = loader.load(filename=rooms_file)
    data_to_conversion = related_json_data(students, rooms)
    try:
        if out_format.lower() == 'json':
            conversion_json.write(data_to_conversion, filename)
        elif out_format.lower() == "xml":
            conversion_xml.write(data_to_conversion, filename)
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
