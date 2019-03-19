import socket

def main():
    ip_port = ('127.0.0.1', 8080)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(ip_port)

    while True:
        inp = input('please input message:').strip()
        if not inp:
            continue
        sk.sendall(inp.encode())

        if inp == 'exit':
            print('communication is over')
            break

        server_reply = sk.recv(1024).decode()
        print(server_reply)

    sk.close()


if __name__ == '__main__':
    main()