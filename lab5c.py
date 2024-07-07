#!/usr/bin/env python3
# Author ID: Agwong-lam

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'

    try:
        number1 = int(number1)
        number2 = int(number2)
        not_int = number1 + number2
        return not_int
    except:
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'

    try:
        f = open(filename, 'r')
        file_content = f.readlines()
        f.close()
        return file_content
    except:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
