'''
Programa que encuentra subdominios de un sitio
Explicar que hace este script: 
'''
import requests
from os import path
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(description="Archivo procesador")
parser.add_argument('-t', '--target', help="El archivo por procesar")
args = parser.parse_args()

# print(parser)

'''
multilinea comment
'''


def check_subdomain(subdomain):
    url = f'http://{subdomain}.{args.target}'
    try:
        requests.head(url, timeout=3)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.Timeout:
        print(f'[!] Timeout en {url}')
    else:
        print(f'[+] dominio encontrado: {url}')

def main():
    if args.target:
        if path.exists('./data/subdominios.txt'):
            try:
                with open("./data/subdominios.txt", "r") as word_list:
                    word_list = word_list.read().split('\n')
            except FileNotFoundError:
                print("Error: El archivo subdominios.txt no existe.")
                sys.exit(1)
                
            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(check_subdomain, word_list)

if __name__ == "__main__":
    main()
