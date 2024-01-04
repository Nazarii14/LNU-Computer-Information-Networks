import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    while True:
        message = input("Enter your message: ")
        client.send(message.encode('utf-8'))

        # If the message is 'exit', close the connection
        if message.lower() == 'exit':
            break

        # Receive response from server
        response = client.recv(1024).decode('utf-8')
        print(f"Server's response: {response}")

    # Close the client connection
    client.close()

if __name__ == "__main__":
    main()
