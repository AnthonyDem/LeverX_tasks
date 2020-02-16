Extend the implementation of the Version class (see task_2.py file) to allow it to be used for
semantic comparison.

Example:
>>> Version('1.1.3') < Version('2.2.3')
True

>>> Version('1.3.0') > Version('0.3.0')
True

>>> Version('0.3.0b') < Version('1.2.42')
True

>>> Version('1.3.42') == Version('42.3.1')
False
