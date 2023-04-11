import socket

HOST = '127.0.0.1'
PORT = 8000

clients = []  # list of connected clients

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f'Server listening on port {PORT}')

    while True:
        # accept a new client connection
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        clients.append(conn)

        while True:
            # receive a command from the user
            command = input('Enter a command to send to clients: ')

            # send the command to all connected clients
            for client in clients:
                try:
                    client.sendall(command.encode('utf-8'))
                    # receive the response from the client
                    client.settimeout(5)  # set timeout value to 5 second
                    data = client.recv(1024)
                    if data:
                        print(
                            f'Response from {client.getpeername()}: \n{data.decode("utf-8")}')
                    else:
                        print(f'No data received from {client.getpeername()}')
                except socket.timeout:
                    print(
                        f'Timeout occurred while waiting for response from {client.getpeername()}')
                except socket.error:
                    print(f'Error sending command to {client.getpeername()}')
                    clients.remove(client)
                    break
