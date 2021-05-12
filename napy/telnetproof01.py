import sys
import telnetlib

HOST = "www.python.org"
PORT = "80"

telnetObj=telnetlib.Telnet(HOST,PORT, timeout=1)
message = ("GET /index.html HTTP/1.1\nHost:"+HOST+"\n\n").encode('ascii')
telnetObj.write(message)
output=telnetObj.read_all()
print(output.decode('utf-8'))
telnetObj.close()
