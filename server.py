from socket import *
from threading import Thread

clients = []

def clientHandler(c, addr):
    global clients
    user = c.recv(1024).decode()
    print('New user' + str(user) + str(addr) + 'entered chat')
    try:
        while True:
            data = c.recv(1024).decode()
            if not data:
                break
            print('User: ' + str(user) + ' Message: ' + str(data))
            message = '[%s] %s' % (str(user), str(data))
            c.send(message.encode())
    except:
        print ('%s left chat' %(user))

HOST = '127.0.0.1'
PORT = 8000

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

print('New server session: '+ str(PORT))

trds = []

for i in range(10):
    c, addr = s.accept()
    clients.append(addr)
    t = Thread(target=clientHandler, args = (c, addr))
    trds.append(t)
    t.start()

for t in trds:
    t.join()

s.close()
