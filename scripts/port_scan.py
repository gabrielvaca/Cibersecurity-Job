import socket
import sys
import argparse
from os import path

current_dir = path.dirname(path.abspath(__file__))
path_file = path.join(current_dir, '../data/ports.txt')

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', required=True, help='Introduce la dirección IP o dominio de la víctima')
args = parser.parse_args()

def scanneer(target):
    if path.exists(path_file):
        try:
            with open(path_file, 'r') as portlist:
                ports = portlist.read().splitlines()

            if len(ports) == 0:
                print('[-] El archivo ports.txt está vacío o no contiene puertos válidos.')
                sys.exit(1)

            for port in ports:
                try:
                    s = socket.socket()
                    s.settimeout(0.5)
                    s.connect((target, int(port)))
                    s.close()
                    print(f'[+] {target}:{port} está abierto')
                except (socket.timeout, socket.error):
                    print(f'[-] {target}:{port} no está disponible o está cerrado')

        except Exception as e:
            print(f'[-] Error al procesar el archivo de puertos o la conexión: {e}')
            sys.exit(1)
    else:
        print('[-] No se encontró el archivo ports.txt')
        sys.exit(1)

def main():
    scanneer(args.target)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[-] Saliendo...')
        sys.exit(1)