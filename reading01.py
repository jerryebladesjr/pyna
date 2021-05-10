#!/usr/bin/env python3
"""Reading in and writing out files"""

def main():
    # old method for opening files
    # requires closing the file object when done
    myfile = open("vendor.txt", 'r')

    # new method for opening files
    # closes file when indentation ends
    with open('vendor-ips.txt', 'w') as myoutfile:
        for line in myfile.readlines():
            splitline = line.split(' ')
            myoutfile.write(splitline[-1] + '\n')

    # close the open file object
    myfile.close()
main()
