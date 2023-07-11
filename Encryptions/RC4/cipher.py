import socket
from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes

HOST = 'localhost'
PORT = 9000
KEY = b'Sixteen byte key'
IV = get_random_bytes(16)

def encrypt_file(filename):
    
    with open(filename, 'rb') as f:
        plaintext = f.read()

    cipher = ARC4.new(KEY)

    ciphertext = cipher.encrypt(plaintext)

    return ciphertext

def send_file(ciphertext):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((HOST, PORT))

    sock.sendall(ciphertext)

    sock.close()

if __name__ == '__main__':
    
    filename = input('Nama file untuk di encrypt: ')

    ciphertext = encrypt_file(filename)

    send_file(ciphertext)
