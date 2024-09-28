import socket
import sys
import argparse

def banner_grabbing(target, port):
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((target, int(port)))
        banner = sock.recv(1024)
        print(f"Banner recibido desde {target}:{port}:\n{banner.decode().strip()}")
    except socket.timeout:
        print(f"Timeout: No se pudo recibir el banner desde {target}:{port}.")
    except Exception as e:
        print(f"Error al conectar con {target}:{port}. Detalles: {e}")
    finally:
        if sock:
            sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Banner grabbing desde un dominio y puerto")
    parser.add_argument('-t', '--target', required=True, help="Dominio o IP objetivo")
    parser.add_argument('-p', '--port', required=True, help="Puerto a conectar")
    args = parser.parse_args()

    banner_grabbing(args.target, args.port)
