import socket

ip_port = ('127.0.0.1', 9999)

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    inp = input('send message：').strip()
    sk.sendto(inp.encode(), ip_port)
    if inp == 'exit':
        break
    data = sk.recv(1024).strip().decode()
    print(data)

sk.close()