#!/usr/bin/env python3
"""Reading in and writing out JSON"""
import json

def main():
    with open("status.json", "r") as myfile:
        myjson = json.load(myfile)

    downservers=[]

    for k,v in myjson :
        if myjson[k][v] is "state" :
            downservers.append(myjson[k][v])

    with open("downed_servers.json", "w") as myfile:
        for ds in downservers :
            myfile.write(str(json.dump(ds)))

main()
