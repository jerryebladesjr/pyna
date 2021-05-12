import sys
import telnetlib

# StarTrek telnet session
# http://mtrek.com/guides/getting-started/

HOST = "mtrek.com"
PORT = "1701"

telnetObj=telnetlib.Telnet(HOST,PORT)
#telnetObj.write(message)

## REALLY great at hanging
# output=telnetObj.read_all()

try:
    output=telnetObj.read_until(b"Ship name: ")

    print(output.decode('utf-8'))

    cmdtopass = input("> ") + "\r"

    telnetObj.write(cmdtopass.encode('ascii'))

    output=telnetObj.read_until(b"Player: ")

    print(output.decode('utf-8'))

    cmdtopass = input("> ") + "\r"

    telnetObj.write(cmdtopass.encode('ascii'))

except Exception as err:
    print(err)

finally:
    # Always close your session!
    telnetObj.close()

