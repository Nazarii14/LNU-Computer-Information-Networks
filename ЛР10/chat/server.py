import socket
import threading

# Function to handle incoming messages from clients
def handle_client(client_socket):
    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received message: {message}")

        # If the message is 'exit', close the connection
        if message.lower() == 'exit':
            break

        # Send a response to the client
        response = input("Enter your response: ")
        client_socket.send(response.encode('utf-8'))

    # Close the client connection
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(5)
    print("Server listening...")

    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")

        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()
