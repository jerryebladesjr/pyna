#!/usr/bin/python3

# Python standard library
import re

with open('networktrace.txt') as trace:
    for line in trace:
        conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', line)
        if conobj:
            print(conobj.group())
            print("The phone number is...")
            print(conobj.group(1))
            print("The IPv6 is...")
            print(conobj.group(2))
            print("The port is...")
            print(conobj.group(3))

