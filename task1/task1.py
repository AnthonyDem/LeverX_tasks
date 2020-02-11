import argparse
import LoadData as ld
import ConversionData as cd
import Exceptions as ex

loader = ld.LoadJSON()
conver_json = cd.JSONConversion()
conver_xml = cd.XMLConversion()


def related_data(students, rooms):
    for room in rooms:
        room['students'] = []
    for student in students:
        studroom = student.get('room')
        for room in rooms:
            if room.get('id') == studroom:
                room.get('students').append(student)
            else:
                continue
    return rooms


def main(students_file, rooms_file, out_format):
    filename = 'output.' + out_format
    students = loader.load(filename=students_file)
    rooms = loader.load(filename=rooms_file)
    data = related_data(students, rooms)
    try:
        if out_format.lower() == 'json':
            conver_json.write(data, filename)
        elif out_format.lower() == "xml":
            conver_xml.write(data, filename)
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
