import argparse
import socket


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('hostname', default='127.0.0.1', help='host name or IP address')
    arg_parser.add_argument('port', type=int)
    arg_parser.add_argument('message', help='message for sending to hostname')
    args = arg_parser.parse_args()

    with socket.socket() as s:
        s.connect((args.hostname, args.port))
        s.send(args.message.encode())
        answer = s.recv(1024).decode()
        print(answer)


if __name__ == '__main__':
    main()
