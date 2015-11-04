#!/usr/bin/python
#Filename:helloworld.py
print('helloworld')

if __name__ == '__main__':
    print(__name__)
    print('This program is being run by itself')
else:
    print(__name__)
    print('I am being imported from another module')
