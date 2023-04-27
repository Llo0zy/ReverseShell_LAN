import socket

sock = socket(socket.AF_INET, socket.SOCK_STREAM)

def upload_file(file_name): # upload file to server
    f = open(file_name, 'rb') 
    sock.send(f.read()) # send to the server

def download_file(file_name): # download file to server
    f = open(file_name, 'wb')
    sock.settimeout(1)
    chunk = sock.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = sock.recv(1024)
        except socket.timeout as e:
            break
    sock.settimeout(None)
    f.close()