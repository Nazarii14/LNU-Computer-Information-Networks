from socket import *
import threading

users = {
    "Rosaka": {
        "Name": "Nazarii",
        "Surname": "Protskiv",
        "Age": 19,
        "Password": "myPassword"
    },
    "dixen18": {
        "Name": "Roman",
        "Surname": "Dix",
        "Age": 21,
        "Password": "dixenCoolGuy1234"
    }
}

address = "localhost"
port = 5555
ip_end = (address, port)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ip_end)
server.listen()
print("Server is listening...")


def handle_client(client_socket, client_address):
    print(f"New connection: {client_address}")

    print("Waiting for username...")
    username = client_socket.recv(1024).decode("utf-8")

    print("Waiting for password...")
    password = client_socket.recv(1024).decode("utf-8")

    if username in users:
        if users[username]["Password"] == password:
            print("User is logged in!")
            client_socket.send(f"Hello {users[username]['Name']} {users[username]['Surname']}".encode("utf-8"))
        else:
            print("User entered wrong password!")
            client_socket.send("False".encode("utf-8"))
    else:
        print("User is not registered!")
        client_socket.send("False".encode("utf-8"))

    client_socket.close()
    print(f"Connection closed: {client_address}")


def sequential_server():
    while True:
        client_socket, client_address = server.accept()
        handle_client(client_socket, client_address)


def threaded_server():
    while True:
        client_socket, client_address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

mode = input("Choose mode (sequential/threaded): ").lower()


if mode == "sequential":
    print("Server is running in sequential mode...")
    sequential_server()
elif mode == "threaded":
    print("Server is running in threaded mode...")
    threaded_server()
else:
    print("Invalid mode!")

