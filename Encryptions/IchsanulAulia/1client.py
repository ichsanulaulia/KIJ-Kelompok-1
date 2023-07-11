import socket
import select
import sys
from threading import Thread
from des import *
from rsa import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('138.91.38.180', 8081))
name = "ii"

d = des()
r = RSA()

p, q = 3, 11
encrypt = 7
decrypt = r.getPrivateKey(r.totient(p, q), encrypt)
n = r.n(p,q)
publicKey = str(encrypt) + " " + str(n)
privateKey = str(decrypt) + " " + str(n)
counterRecv = 0

myKey = "AABB09182736CCDD"
friendPublicKey = ""
friendKey = ""

# print(privateKey, publicKey)

def send_msg(sock):
	while True:
		data = input()
		if(data == "start"):
			sock.send(publicKey.encode())
		elif(data == "send"):
			sock.send(r.send(myKey, friendPublicKey).encode())
		else:
			sock.send((name + ' ' + d.encrypt(data, friendKey, 1)).encode())
		sys.stdout.flush()

def recv_msg(sock):
	
	while True:
		global counterRecv
		global friendPublicKey
		global friendKey
		if(counterRecv == 0):
			data = sock.recv(2048).decode()
			sys.stdout.write(data + '\n')
			counterRecv = 1
			friendPublicKey = data
			# print(friendPublicKey)
		elif(counterRecv == 1):
			data = sock.recv(2048).decode()
			# print(data)
			friendKey = r.receive(data, privateKey)
			# print(friendKey)
			counterRecv = 2
		else:
			data = sock.recv(2048).decode().partition(' ')
			name = data[0]
			message = data[2]
			sys.stdout.write(name + ' : ' + d.encrypt(message, myKey, 2) + '\n')

Thread(target=send_msg, args=(server,)).start()
# Thread(target=recv_msg, args=(server,)).start()

while True:
	sockets_list = [server]
	read_socket, write_socket, error_socket = select.select(sockets_list, [], [])
	for socks in read_socket:
		if socks == server:
			recv_msg(socks)
		else:
			send_msg(socks)

server.close()