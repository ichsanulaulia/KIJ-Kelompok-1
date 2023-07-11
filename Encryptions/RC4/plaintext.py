import socket
from Crypto.Cipher import ARC4

HOST = 'localhost'
PORT = 9000
KEY = b'Sixteen byte key'

def decrypt_file(ciphertext):
    
    cipher = ARC4.new(KEY)

    plaintext = cipher.decrypt(ciphertext)

    return plaintext

def receive_file():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((HOST, PORT))

    sock.listen(1)

    conn, addr = sock.accept()

    with conn:
        print('Connected by', addr)
        
        data = b''
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            data += chunk

    plaintext = decrypt_file(data)

    return plaintext

if __name__ == '__main__':
    
    plaintext = receive_file()

    with open('output.jpg', 'wb') as f:
        f.write(plaintext)
