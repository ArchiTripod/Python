#!/usr/bin/python
#Filename:recursive_import.py

#1. to see wether helloworld_imported will call helloworld
#   if so ,means recursive import is possible
import helloworld_imported

#2. to see wether multiple imports will be called.
#   since helloworld_import has import helloworld once, this time helloworld
#   will not be called
import helloworld


if __name__ == '__main__':
    print(__name__)
    print('This program is being run by itself')
else:
    print(__name__)
    print('I am being imported from another module')
