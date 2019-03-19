import socket
import threading


def conn_handler(conn, client):
    print('request from client[{}:{}]'.format(client[0], client[1]))
    while True:
        client_data = conn.recv(1024).decode()
        if client_data == 'exit':
            print('communicate with [{}:{}] is over'.format(client[0], client[1]))
            break
        print('message from client [{}:{}]: {}'.format(client[0], client[1], client_data))
        conn.sendall('server already received your message'.encode())
    conn.close()


def main():
    ip_port = ('127.0.0.1', 8080)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(ip_port)
    sk.listen(5)
    print('start socket service, waiting for client connecting')

    while True:
        conn, address = sk.accept()
        t = threading.Thread(target=conn_handler, args=(conn, address))
        t.start()


if __name__ == '__main__':
    main()