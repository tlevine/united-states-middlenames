import os

def readfiles(directory, loadfunc):
    'Go throug all of the files and import everything.'
    for filepart in range(1, 4):
        f = open(os.path.join(directory, 'ssdm%d' % filepart), 'r')
        for line in f:
            loadfunc(line[:-1]) # The last character is a \n
