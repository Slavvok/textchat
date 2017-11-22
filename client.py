from socket import *

def Main():
    host = '127.0.0.1'
    port = 8000
    s = socket()
    s.connect((host,port))     #Connecting to server
    user = input ("Input your name: ")  #Username to use for chatting
    s.send(user.encode())   #Encode converts values from str to bytes
    data = input(" -> ")
    while data != 'q':
        s.send(data.encode())
        message = s.recv(1024).decode() #Decode converts values from bytes to str
        print (" Server answer: " + message)
        data = input(" -> ")
    s.close()

if __name__ == '__main__':
    Main()
