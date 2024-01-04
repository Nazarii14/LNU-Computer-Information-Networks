from socket import *

address = "localhost"
port = 5555
ip_end = (address, port)
s = socket(AF_INET, SOCK_STREAM)
s.connect(ip_end)
print("Connected to server!")

username = input("Enter username: ")
s.send(username.encode("utf-8"))

password = input("Enter password: ")
s.send(password.encode("utf-8"))

print("Waiting for response...")
response = s.recv(1024).decode("utf-8")
print(response)
s.close()


