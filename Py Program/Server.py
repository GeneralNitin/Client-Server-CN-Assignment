from ast import If
from http import server
from socket import *
serverName = 'localhost'
serverPort = 8888
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("The Server is ready to Receive Messages: ")
connectionSocket, addr = serverSocket.accept()
while True:
    sentence = connectionSocket.recv(1024).decode()
    print("Message from Client", sentence)
    sentence = input('Enter Message For Client: ') 
    if sentence.upper() == "EXIT":
        break
    connectionSocket.send(sentence.encode()) 
connectionSocket.close()