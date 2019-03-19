import socket

ip_port = ('127.0.0.1', 9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(ip_port)

while True:
    data, addr = sk.recvfrom(1024)
    print("message from {}:".format(addr) + data.strip().decode())
    if data == 'exit':
        print('client disconnect ')
        break
    reply_msg = 'hello {}'.format(addr)
    sk.sendto(reply_msg.encode(), addr)

sk.close()