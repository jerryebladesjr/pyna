#!/usr/bin/python3

# Python standard library
import re

# hardcode the string we'll search through
contact = "Contact: <sip:+17175664428@[2600:2304:9210:ec::2]:5060;eri-generated-at=10.172.0.132>"

# parse out the contact string using our regex logic
conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', contact)

# searches test True if they find a match
# False if no match
if conobj:
    # display the match
    print(conobj.group())
    print("The phone number is...")
    print(conobj.group(1))
    print("The IPv6 is...")
    print(conobj.group(2))
    print("The port is...")
    print(conobj.group(3))

