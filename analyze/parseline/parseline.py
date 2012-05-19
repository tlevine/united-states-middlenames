'Import the death file into a MongoDB.'
from unittest import TestCase

def parseline(line):
    pass   


class TestLine(TestCase):
    line = ' 001010001MUZZEY                  GRACE                          1200197504161902                   '

    def test_padding(self):
        padding0 = self.line[0]
        self.assertEqual(padding0, ' ')

    def test_ssn(self):
        'Is the SSN column what we expect?'
        ssn = self.line[1:10]
        self.assertRegexpMatches(ssn, r'[0-9]+')

    def test_name(self):
        name = self.line[10:65]
        self.assertRegexpMatches(name, r'[A-Z ]+')

    def test_dates(self):
        deathdatetime = self.line[65:81]
        self.assertRegexpMatches(deathdatetime, r'[0-9]+')
