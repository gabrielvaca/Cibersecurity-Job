# %%
import subprocess


def busqueda_subdominios():
    try:
        print("Ejecutando bsqueda de subdominios...")
        target = input("Ingrese el dominio objetivo (sin 'http://'): ")
        subprocess.run(["python3", "./scripts/subdominios.py", "-t", target])
    except FileNotFoundError:
        print("Error: No se encontró el script de búsqueda de subdominios.")

def banner_grabbing():
    try:
        print("Ejecutando banner grabbing...")
        target = input("Ingrese el dominio o IP objetivo: ")
        port = input("Ingrese el puerto: ")
        subprocess.run(["python3", "./scripts/bannergrabbing.py", "-t", target, "-p", port])
    except FileNotFoundError:
        print("Error: No se encontró el script de banner grabbing.")

# def wad_discovery():
#     try:
#         print("Ejecutando WAD - Web Application Discovery...")
#         subprocess.run(["python3", "./scripts/wad.py"])
#     except FileNotFoundError:
#         print("Error: No se encontro el script de WAD.")

def escaneo_puertos():
    try:
        print("Ejecutando escaneo de puertos...")
        target = input("Ingrese el dominio o IP objetivo para el escaneo de puertos: ")
        subprocess.run(["python3", "./scripts/port_scan.py", "-t", target])
    except FileNotFoundError:
        print("Error: No se encontro el script de escaneo de puertos.")

# def escaneo_vulnerabilidades():
    
#     print("Ejecutando escaneo de vulnerabilidades...")
    
def get_ip_using_nslookup():
    try:
        print("Ejecutando nslookup para obtener la IP...")
        target = input("Ingrese el dominio o IP objetivo: ")
        subprocess.run(["python3", "./scripts/get_ip_2.py", "-t", target])
    except FileNotFoundError:
        print("Error: No se encontró el script para obtener la IP usando nslookup.")

def get_ip_using_socket():
    try:
        print("Ejecutando obtención de IP usando socket...")
        target = input("Ingrese el dominio o IP objetivo: ")
        subprocess.run(["python3", "./scripts/get_ip.py", "-t", target])
    except FileNotFoundError:
        print("Error: No se encontró el script para obtener la IP usando socket.")

def main():
    print("Sistema para pruebas de seguridad informática")
    print("Desarrollado por: Gabriel VV")
    while True:
        print("\nMenú:")
        print("1. Busqueda de subdominios")
        print("2. Banner grabbing")
        # print("3. WAD - Web Application Discovery")
        print("4. Escaneo de puertos")
        # print("5. Escaneo de vulnerabilidades")
        print("6.- Get IP using nslookup")
        print("7.- Get IP using socket")
        print("8. Salir")
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                busqueda_subdominios()
            case "2":
                banner_grabbing()
            # case "3":
            #     print("Ahorita no padrino")
            case "4":
                escaneo_puertos()
            # case "5":
            #     print("Ahorita no padrino")
            case "6":
                get_ip_using_nslookup()
            case "7":
                get_ip_using_socket()
            case "8":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida. Intentelo de nuevo.")

if __name__ == "__main__":
    main()
# %%
