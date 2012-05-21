from parseline import parseline
import unittest
import datetime

class BaseLineTest(unittest.TestCase):
#    line = ''
#    expected_result = {
#        'ssn': '',
#        'surname': '',
#        'forename': '',
#        'middles': [],
#        'born': {'year': None, 'month': None, 'day': None},
#        'died': {'year': None, 'month': None, 'day': None},
#    }

    def test_valid_line(self):
        '''
        Line validity is something the parser should handle, but
        let's put this in because it might help with debugging.
        '''
        self.assertEqual(len(self.line), 100)
        self.assertEqual(self.line[0], ' ')
        self.assertNotEqual(self.line[-1], '\n')

    def test_parser(self):
        self.assertDictEqual(parseline(self.line), self.expected_result)

#class Test001010001(BaseLineTest):
    'This is the first one! It has a missing value.'
    line = ' 001010001MUZZEY                  GRACE                          1200197504161902                   '
    expected_result = {
        'ssn': '001010001',
        'surname': 'MUZZEY',
        'forename': 'GRACE',
        'middles': [],
        'born': {'year': 1902, 'month': 4, 'day': 16},
        'died': {'year': 1975, 'month': 12, 'day': None}, #Missing value
    }

class Test242250680(BaseLineTest):
    line = ' 242250680TATE                    RONNIE         D              V1113200211161957                   '
    expected_result = {
        'ssn': '242250680',
        'surname': 'TATE',
        'forename': 'RONNIE',
        'middles': ['D', 'V'],
        'born': {'year': 1957, 'month': 11, 'day': 16},
        'died': {'year': 2002, 'month': 11, 'day': 13}, #Missing value
    }

class Test001014420(BaseLineTest):
    line = ' 001014420DENSMORE-PHI            ELEANOR                       V1101200209021915                   '
    expected_result = {
        'ssn': '001014420',
        'surname': 'DENSMORE-PHI',
        'forename': 'ELEANOR',
        'middles': ['V'],
        'born': {'year': 1915, 'month':  9, 'day': 2},
        'died': {'year': 2002, 'month': 11, 'day': 1}, #Missing value
    }

class BaseInvalidLineTest(unittest.TestCase):
    def test_padding0(self):
        with self.assertRaises(ValueError):
            parseline('242250680TATE                    RONNIE         D              V1113200211161957                   ')

    def test_padding0(self):
        with self.assertRaises(ValueError):
            parseline('242250680TATE                    RONNIE         D              V1113200211161957                   ')

    def test_ssn(self):
        with self.assertRaises(ValueError):
            parseline(' 9 2250680TATE                    RONNIE         D              V1113200211161957                   ')

    def test_names(self):
        with self.assertRaises(ValueError):
            parseline(' 242250680TATE                    Ronnie         D              V1113200211161957                   ')
        with self.assertRaises(ValueError):
            parseline(' 242250680TATE            6       RONNIE         D              V1113200211161957                   ')
        with self.assertRaises(ValueError):
            parseline(' 242250680TATE                     RONNIE         D              V1113200211161957                   ')

    def test_datetimes(self):
        with self.assertRaises(ValueError):
            parseline(' 242250680TATE                    RONNIE         D              V13132002111619572                  ')

    def test_padding1(self):
        with self.assertRaises(ValueError):
            parseline(' 242250680TATE                    RONNIE         D              V1113200211161957          _        ')

    def test_length(self):
        with self.assertRaises(ValueError):
            parseline(' 242250680TATE                    RONNIE         D              V1113200211161957                      ')


if __name__ == '__main__':
    unittest.main()
