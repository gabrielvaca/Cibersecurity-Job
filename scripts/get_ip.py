import argparse
import socket
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Introduce la URL sin http://')
args = parser.parse_args()

def get_ip(target):
    try:
        ip = socket.gethostbyname(target)
        print(f'[+] IP de {target}: {ip}')
    except socket.gaierror:
        print('[-] No se pudo obtener la IP, por favor verifica la URL.')
        sys.exit(1)

def main():
    if args.target:
        get_ip(args.target)
    else:
        print('[-] Debes indicar la URL.')
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[-] Saliendo...')
        sys.exit(1)