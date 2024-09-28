import requests
import argparse

def check_path(target, path):
    url = f'http://{target}/{path}'
    try:
        response = requests.head(url, timeout=3)
        if response.status_code == 200:
            print(f'[+] {url} encontrado')
    except requests.exceptions.RequestException as e:
        print(f'[-] Error en {url}: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WAD - Descubrimiento de aplicaciones web")
    parser.add_argument('-t', '--target', required=True, help="Dominio objetivo")
    args = parser.parse_args()

    common_paths = ['admin', 'login', 'dashboard', 'config', 'index.html', 'robots.txt']

    for path in common_paths:
        check_path(args.target, path)
