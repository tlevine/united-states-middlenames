#!/usr/bin/env python3
from bisect import bisect_left

LOCATIONS = [
    (('000', '000'), 'unused'),
    (('001', '003'), 'NH'),
    (('004', '007'), 'ME'),
    (('008', '009'), 'VT'),
    (('010', '034'), 'MA'),
    (('035', '039'), 'RI'),
    (('040', '049'), 'CT'),
    (('050', '134'), 'NY'),
    (('135', '158'), 'NJ'),
    (('159', '211'), 'PA'),
    (('212', '220'), 'MD'),
    (('221', '222'), 'DE'),
    (('223', '231'), 'VA'),
    (('232', '236'), 'WV'),
    (('237', '246'), 'NC'),
    (('247', '251'), 'SC'),
    (('252', '260'), 'GA'),
    (('261', '267'), 'FL'),
    (('268', '302'), 'OH'),
    (('303', '317'), 'IN'),
    (('318', '361'), 'IL'),
    (('362', '386'), 'MI'),
    (('387', '399'), 'WI'),
    (('400', '407'), 'KY'),
    (('408', '415'), 'TN'),
    (('416', '424'), 'AL'),
    (('425', '428'), 'MS'),
    (('429', '432'), 'AR'),
    (('433', '439'), 'LA'),
    (('440', '448'), 'OK'),
    (('449', '467'), 'TX'),
    (('468', '477'), 'MN'),
    (('478', '485'), 'IA'),
    (('486', '500'), 'MO'),
    (('501', '502'), 'ND'),
    (('503', '504'), 'SD'),
    (('505', '508'), 'NE'),
    (('509', '515'), 'KS'),
    (('516', '517'), 'MT'),
    (('518', '519'), 'ID'),
    (('520', '520'), 'WY'),
    (('521', '524'), 'CO'),
    (('525', '525'), 'NM'),
    (('526', '527'), 'AZ'),
    (('528', '529'), 'UT'),
    (('530', '530'), 'NV'),
    (('531', '539'), 'WA'),
    (('540', '544'), 'OR'),
    (('545', '573'), 'CA'),
    (('574', '574'), 'AK'),
    (('575', '576'), 'HI'),
    (('577', '579'), 'DC'),
    (('580', '580'), 'VI'), # Virgin Islands
    (('581', '584'), 'PR'), # Puerto Rico
    (('585', '585'), 'NM'),
    (('586', '586'), 'PI'), # Pacific Islands*
    (('587', '588'), 'MS'),
    (('589', '595'), 'FL'),
    (('596', '599'), 'PR'), # Puerto Rico
    (('600', '601'), 'AZ'),
    (('602', '626'), 'CA'),

    (('627', '699'), 'unassigned'), #for future use
    (('700', '728'), 'railroad'), #Railroad workers through 1963, then discontinued
    (('729', '899'), 'unassigned'), #for future use
    (('900', '999'), 'invalid') #**

    # * Guam, American Samoa,
    # Northern Mariana Islands,
    # Philippine Islands

    # ** not valid SSNs, but were used for program purposes
    # when state aid to the aged, blind and disabled was
    # converted to a federal program administered by SSA.

]

high_values = {k[1]:v for k,v in LOCATIONS}
high_keys = list(high_values.keys()); high_keys.sort()

def ssn_to_state(ssn):
    return high_values[high_keys[bisect_left(high_keys, ssn[:3])]]


def tests():
    fixtures = [('000', 'unused'), ('581', 'PR'), ('584', 'PR'), ('446', 'OK'), ('626', 'CA')]
    for ssn, state in fixtures:
        assert ssn_to_state(ssn) == state


if __name__ == '__main__':
    import sys
    print(ssn_to_state(sys.argv[1]))
    tests()
