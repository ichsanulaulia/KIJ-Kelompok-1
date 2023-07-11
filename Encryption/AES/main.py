import socket
from Crypto.Cipher import AES

HOST = 'localhost'
PORT = 9000
KEY = b'Sixteen byte key'

def receive_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        conn, addr = sock.accept()
        with conn:
            iv = conn.recv(16)
            ciphertext = b''
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                ciphertext += data

    cipher = AES.new(KEY, AES.MODE_CBC, IV=iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = padded_plaintext.rstrip(b'\0')

    return plaintext

if __name__ == '__main__':
    plaintext = receive_file()
    with open('decrypted_file', 'wb') as f:
        f.write(plaintext)
