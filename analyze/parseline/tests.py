from parseline import parseline
import unittest
import datetime

class BaseLineTest(unittest.TestCase):
    line = ''
    expected_result = {}

    def test_valid_line(self):
        '''
        Line validity is something the parser should handle, but
        let's put this in because it might help with debugging.
        '''
        self.assertEqual(len(self.line), 101)
        self.assertEqual(self.line[0], ' ')
        self.assertEqual(self.line[-1], '\n')

    def test_parser(self):
        self.assertDictEqual(parseline(line), expected_result)

class Test001010001(BaseLineTest):
    line = ' 001010001MUZZEY                  GRACE                          1200197504161902                   '
    expected_result = {
        'ssn': '001010001',
        'surname': 'MUZZEY',
        'forename': 'GRACE',
        'middles': []
        'born': {'year': 1902, 'month': 4, 'day': 16},
        'died': {'year': 1975, 'month': 12, 'day': None}, #Missing value
    }

if __name__ == 'main':
    unittest.main()
