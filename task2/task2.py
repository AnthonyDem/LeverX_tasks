from copy import  deepcopy
from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        self.version, self.spliter = self.convert_in_one_format(version)
        self.version_number, self.residue = self.split_version(self.version)

    def __eq__(self, other):
        min_len = min(len(self.version_number), len(other.version_number))
        if len(self.version_number) == len(other.version_number):
            if self.version_number == other.version_number:
                return self.version_number == other.version_number
            elif not self.residue:
                return False
            elif not other.residue:
                return False
            else:
                return self.residue == other.residue
        elif len(self.version_number) != len(other.version_number):
            if self.version_number[:min_len] == other.version_number[:min_len]:
                return self.version_number[:min_len] == other.version_number[:min_len]
            elif not self.residue:
                return False
            elif not other.residue:
                return False
            else:
                return self.residue == other.residue

    def __lt__(self, other):
        min_len = min(len(self.version_number), len(other.version_number))
        if len(self.version_number) == len(other.version_number):
            if self.version_number != other.version_number:
                return self.version_number < other.version_number
            elif not self.residue:
                return False
            elif not other.residue:
                return True
            else:
                return self.residue < other.residue
        elif len(self.version_number) != len(other.version_number):
            if self.version_number[:min_len] != other.version_number[:min_len]:
                return self.version_number[:min_len] < other.version_number[:min_len]
            elif not self.residue:
                return False
            elif not other.residue:
                return True
            else:
                return self.residue < other.residue

    def convert_in_one_format(self, version):
        spl = 0
        transfers = {'a': '-alpha', 'b': '-beta', 'rc': '-rc'}
        transfers_to_digit = {'-alpha': '.1', '-beta': '.2', '-rc': '.3'}
        for i in version:
            if i.isdigit():
                spl += 1
            elif i.isalpha():
                break
            else:
                continue
        if version.find('-') == -1:
            for key, value in transfers.items():
                version = version.replace(key, value)
        for key, value in transfers_to_digit.items():
            version = version.replace(key, value)
        return version, spl

    def split_version(self, version):
        splited_version = version.split('.')
        splited_version = [int(item) if item.isdigit() else str(item) for item in splited_version]
        version_number = splited_version[:self.spliter]
        if splited_version[self.spliter:]:
            residue = splited_version[self.spliter:]
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
        ('1.0', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), 'le failed'
        assert Version(version_2) > Version(version_1), 'ge failed'
        assert Version(version_2) != Version(version_1), 'neq failed'
        assert Version(version_1) == Version(version_2), 'eq failed'



if __name__ == "__main__":
    main()
