from socket import *

def Main():
    host = '127.0.0.1'
    port = 8000
    s = socket()
    s.connect((host,port))
    user = input ("Input your name: ")
    s.send(user.encode())
    data = input(" -> ")
    while data != 'q':
        s.send(data.encode())
        message = s.recv(1024).decode()
        print (" Server answer: " + message)
        data = input(" -> ")
    s.close()

if __name__ == '__main__':
    Main()
