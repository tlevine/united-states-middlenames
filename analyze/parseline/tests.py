from parseline import parseline
import unittest
import datetime

class BaseLineTest(unittest.TestCase):
    line = ''
    expected_result = {
        'ssn': '',
        'surname': '',
        'forename': '',
        'middles': [],
        'born': {'year': None, 'month': None, 'day': None},
        'died': {'year': None, 'month': None, 'day': None},
    }

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

class Test001010001(BaseLineTest):
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

class BaseInvalidLineTest(unittest.TestCase):
    line = ''

if __name__ == '__main__':
    unittest.main()
