"""
Script de escaneo de subred con Nmap usando python-nmap
Cumple requisitos de auditoría ética y uso seguro en entornos controlados.
"""
import nmap
import sys
import socket
import os

# Validar si Nmap está instalado
from shutil import which

def check_nmap_installed():
    # Verificar si nmap está en el PATH
    if which('nmap') is not None:
        return 'nmap'
    
    # Si no está en PATH, verificar rutas comunes de Windows
    common_paths = [
        r"C:\Program Files (x86)\Nmap\nmap.exe",
        r"C:\Program Files\Nmap\nmap.exe"
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            print(f"[INFO] Nmap encontrado en: {path}")
            return path
    
    print("[ERROR] Nmap no está instalado o no está en el PATH del sistema.")
    print("[INFO] Instala Nmap desde: https://nmap.org/download.html")
    sys.exit(1)

# Validar si la subred es accesible
def check_network_accessible(target_subnet):
    try:
        # Intentar resolver la IP base
        base_ip = target_subnet.split('/')[0]
        socket.gethostbyname(base_ip)
    except Exception as e:
        print(f"[ERROR] No se puede acceder a la red objetivo: {e}")
        sys.exit(1)

# Función principal de escaneo
def scan_subnet(subnet, nmap_path='nmap'):
    nm = nmap.PortScanner(nmap_search_path=(nmap_path,) if nmap_path != 'nmap' else ())
    print(f"[INFO] Iniciando escaneo en la subred {subnet} (esto puede tardar)...")
    try:
        # -sV: detección de versiones
        nm.scan(hosts=subnet, arguments='-sV')
    except Exception as e:
        print(f"[ERROR] Fallo al ejecutar el escaneo: {e}")
        sys.exit(1)

    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    activos = [h for h, estado in hosts_list if estado == 'up']
    print(f"\n[INFO] Hosts activos encontrados: {len(activos)}\n")
    for host in activos:
        print(f"Host: {host}")
        print("  Puertos abiertos:")
        if 'tcp' in nm[host]:
            for port in sorted(nm[host]['tcp'].keys()):
                port_data = nm[host]['tcp'][port]
                service = port_data.get('name', 'Desconocido')
                version = port_data.get('version', '')
                product = port_data.get('product', '')
                extrainfo = port_data.get('extrainfo', '')
                ver_str = f"{product} {version} {extrainfo}".strip()
                print(f"    - Puerto {port}/tcp: {service} | Versión: {ver_str if ver_str else 'No detectada'}")
        else:
            print("    No se detectaron puertos abiertos TCP.")
        print("-"*50)
    print(f"\n[RESUMEN] Total de hosts escaneados: {len(hosts_list)}")
    print(f"[RESUMEN] Total de hosts activos: {len(activos)}")

if __name__ == "__main__":
    # Parámetro de subred por línea de comandos o por defecto
    if len(sys.argv) > 1:
        subnet = sys.argv[1]
    else:
        subnet = "192.168.1.0/24"  # Cambia esto según tu entorno
    
    nmap_path = check_nmap_installed()
    check_network_accessible(subnet)
    scan_subnet(subnet, nmap_path)
