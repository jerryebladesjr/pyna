#!/usr/bin/env python3
## USOpen Tournament Switch Checker -- 2018.05.01
''' usopen.py
This script is being designed to provide the following automated tasks:
- Ping check the router (import os)
- Login check the router (import netmiko)
- Determine if interfaces in use are up (import netmiko)
- Apply new configuration (import netmiko)

The IPs and device type should be made available via a spreadsheet

'''
import os
import bootstrapper

## ADD THE LINE BELOW THIS COMMENT
import bootstrapper

## pyexcel and pyexce-xls are required for our program to execute
# python3 -m pip install --user pyexcel
# python3 -m pip install --user pyexcel-xls
import pyexcel

# python3 -m pip install --user netmiko
from netmiko import ConnectHandler

## retrieve data set from spreadsheet
def retv_excel(par):
    d = {}
    records = pyexcel.iget_records(file_name=par) # create a record object that is an open spreadsheet
    for record in records:
         # adds a new IP and driver key:value pair to our dictionary
        d.update( { record['IP'] : record['driver'] } )
    return d # return the completed dictionary

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False

## Check interfaces - Issue "show ip init brief"
def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        my_command = open_connection.send_command("show ip int brief")       
        my_command2 = open_connection.send_command("show hostname")       
    except:
        my_command = "** ISSUING COMMAND FAILED **"
    finally:
        return my_command2 + "\n" +  my_command


def login_router(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        return True        
    except:
        return False

## Main function - This is the code that runs our functions
def main():

    ## Determine where *.csv input is
    file_location = input("\nWhere is the file location? ")

    ## Entry is now a local dictionary containing IP(key):driver(value)
    entry = retv_excel(file_location)

    ## Use a loop to check each device for SSH accessibility
    print("\n***** BEGIN SSH CHECKING *****")
    for x in entry.keys():
        if login_router(entry[x], x, "admin", "alta3"):
            print("\n\t**IP: - " + x + " - SSH connectivity UP\n")
        else:
            print("\n\t**IP: - " + x + " - SSH connectivity DOWN\n")

    ## Use a loop to check each device for ICMP responses
    print("\n***** BEGIN ICMP CHECKING *****")
    for x in entry.keys():
        if ping_router(x):
            print("\n\t**IP: - " + x + " - responding to ICMP\n")
        else:
            print("\n\t**IP: - " + x + " - NOT responding to ICMP\n")

    ## Use a loop to check each device for ICMP responses
    print("\n***** BEGIN SHOW IP INT BRIEF *****")
    for x in entry.keys():
        print("\n" + interface_check(entry[x], x, "admin", "alta3"))

    ## Determine if new config should be applied && if so apply new config
    print("\n***** NEW BOOTSTRAPPING CHECK *****")
    ynchk = input("\nWould you like to apply a new configuration? y/N ")
    if (ynchk.lower() == "y") or (ynchk.lower() == "yes"):  # if user input yes or y
        conf_loc = input("\nWhere is the location of the new config file? ")
        conf_ip = input("\nWhat is the IP address of the device to be configured? ")

        if bootstrapper.bootstrapper(entry[conf_ip], conf_ip, "admin", "alta3", conf_loc):
            print("\nNew configuration applied!")
        else:
            print("\nProblem in applying new configuration!")

## Call main()
main()

