import socket

s = socket.socket();
print("Socket Created successfully")
s.bind(('',12345))
s.listen(5)
print("Socket is listening")

while True:
    c, address = s.accept()
    print("Got connection from")
    c.send('Thanks for connecting to my socket'.encode())
    c.close()