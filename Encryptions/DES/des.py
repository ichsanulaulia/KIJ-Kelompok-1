import socket
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

HOST = 'localhost'
PORT = 9000
KEY = b'Sixteen byte key'
IV = get_random_bytes(16)

def encrypt_file(filename):
    with open(filename, 'rb') as f:
        plaintext = f.read()

    padded_plaintext = plaintext + b'\0' * (16 - len(plaintext) % 16)

    cipher = AES.new(KEY, AES.MODE_CBC, IV=IV)

    ciphertext = cipher.encrypt(padded_plaintext)

    return ciphertext

def send_file(ciphertext):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(IV)
    sock.sendall(ciphertext)
    sock.close()

if __name__ == '__main__':
    filename = input('File name to encrypt: ')
    file_ext = os.path.splitext(filename)[1].lower()
    
    if file_ext in ['.jpg', '.jpeg', '.mp4']:
        ciphertext = encrypt_file(filename)
        send_file(ciphertext)
    else:
        print("Unsupported file type. Only .jpg and .mp4 files are supported.")
