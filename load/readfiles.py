def readfiles(loadfunc):
    'Go throug all of the files and import everything.'
    for filepart in range(1, 4):
        def o(prefix):
            return open('deathfile/ssdm%d' % filepart, 'r')

        try:
            f = o('/tmp/') # From the ramdisk
        except IOError:
            f = o('') #From the hard disk

        for line in f:
            loadfunc(line[:-1]) # The last character is a \n
