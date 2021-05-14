#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("CREATE TABLE IF NOT EXISTS switches;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("HOST = ", row[1])
    print("IP_ADDRESS = ", row[2])
    print("RUNNING_CONFIG = ", row[3], "\n")
    print("STARTUP_CONFIG = ", row[4], "\n")
    print("VALID = ", row[5], "\n")

print("Operation done successfully")
conn.close()

