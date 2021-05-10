#!/usr/bin/env python3
"""Reading in and writing out JSON"""
import json

def main():
    with open("ciscoex.json", "r") as myfile:
        myjson = json.load(myfile)

    with open("ciscoex.text", "w") as myfile:
        myfile.write(str(myjson["time"]) + " " + myjson["host"] + " " + myjson["type"])

main()
