import socket
import sys
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Connection failed" %err)
    
try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("There was an error")
    sys.exit()
    
s.connect((host_ip, 80))
print("Socket sucessfully connected to Google \ on port ==%s"%host_ip)
    