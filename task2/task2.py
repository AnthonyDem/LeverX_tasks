from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        self.version = self.convert_in_one_format(version)
        self.version_number, self.residue = self.split_version(self.version)

    def __eq__(self, other):
        return self.version == other.version

    def __lt__(self, other):
        if self.version_number != other.version_number:
            return self.version_number < other.version_number
        elif not self.residue:
            return False
        elif not other.residue:
            return True

    @staticmethod
    def convert_in_one_format( version):
        transfers = {'a': '-alpha', 'b': '-beta', 'rc': '-rc'}
        if version.find('-') == -1:
            for key, value in transfers.items():
                version = version.replace(key, value)
        return version

    @staticmethod
    def split_version(version):
        splited_version = version.replace('-', '.').split('.')
        for i in splited_version:
            if i.isdigit():
                i = int(i)

        version_number = splited_version[:3]
        if splited_version[3:]:
            residue = splited_version[3:]
        else:
            residue = []
        return version_number, residue


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1b', '1.0.10-alpha.beta'),
        ('1.0.0-rc.1', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), 'le failed'
        assert Version(version_2) > Version(version_1), 'ge failed'
        assert Version(version_2) != Version(version_1), 'neq failed'


if __name__ == "__main__":
    main()
