from socket import *
from threading import Thread

clients = []    #Clients list

def clientHandler(c, addr):
    global clients
    user = c.recv(1024).decode()
    print('New user' + str(user) + str(addr) + 'entered chat')
    try: #Client session handler. Outputs exception when client leaves
        while True:
            data = c.recv(1024).decode() #Data import
            if not data:
                break
            print('User: ' + str(user) + ' Message: ' + str(data))
            message = '[%s] %s' % (str(user), str(data))
            c.send(message.encode()) #Formatted data output
    except:
        print ('%s has left the chat' %(user))

def Main():
    HOST = '127.0.0.1' #Server's host and port
    PORT = 8000

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)

    print('New server session: '+ str(PORT))

    trds = [] #Threads list

    for i in range(10): #Adding number of threads depending on clients number
        c, addr = s.accept()
        clients.append(addr) #Adding new client
        t = Thread(target=clientHandler, args = (c, addr))
        trds.append(t)
        t.start()

    for t in trds:
        t.join()

    s.close()

if __name__ == '__main__':
    Main()
