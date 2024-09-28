import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Introduce la dirección IP o dominio de la víctima')
args = parser.parse_args()

def get_ip(target):
    try:
        res = os.system(f'nslookup {target}')
        if res != 0:
            print('[-] No se pudo obtener la IP usando nslookup.')
    except Exception as e:
        print(f'[-] Error al ejecutar nslookup: {e}')
        sys.exit(1)

def main():
    if args.target:
        get_ip(args.target)
    else:
        print('[-] Debes indicar la URL o dirección IP.')
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[-] Saliendo...')
        sys.exit(1)
