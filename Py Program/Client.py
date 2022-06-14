from socket import * 
serverName = 'localhost'
serverPort = 8888 
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 
while True:
    sentence = input('Enter message for Server: ')
    if sentence.upper() == "EXIT":
        break
    clientSocket.send(sentence.encode()) 
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode()) 
clientSocket.close()