import subprocess
import platform
import socket
import threading
import time
import re
from mac_vendor_lookup import MacLookup  # Necesitarás instalar esta librería con `pip install mac-vendor-lookup`

# Lista para guardar los dispositivos encontrados
dispositivos_activados = []

# Función para realizar un ping sigiloso (sin ser detectado fácilmente)
def ping_silencioso(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", param, "1", ip]
    try:
        result = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"Dispositivo activo encontrado: {ip}")
            dispositivos_activados.append(ip)
            return ip
    except Exception as e:
        pass
    return None

# Función para obtener la dirección MAC usando el comando arp
def obtener_mac(ip):
    try:
        comando = ["arp", "-a", ip] if platform.system().lower() == "windows" else ["arp", ip]
        result = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = result.stdout
        mac = re.search(r"([a-f0-9]{2}[:-]){5}[a-f0-9]{2}", salida)
        if mac:
            return mac.group(0).upper()
        return "MAC no encontrada"
    except Exception as e:
        return "Error al obtener MAC"

# Función para determinar el tipo de dispositivo según el fabricante MAC
def determinar_tipo_dispositivo(mac):
    try:
        vendor = MacLookup().lookup(mac)
        if any(keyword in vendor.lower() for keyword in ["mobile", "phone", "smart"]):
            return "Móvil"
        elif any(keyword in vendor.lower() for keyword in ["pc", "desktop", "laptop"]):
            return "PC"
        else:
            return "Dispositivo desconocido"
    except Exception as e:
        return "Fabricante no encontrado"

# Función para escanear un rango de IPs
def escanear_red(rango_red):
    print(f"Escaneando el rango {rango_red} para encontrar dispositivos activos...\n")
    base_ip = rango_red.split(".")
    for i in range(1, 255):
        ip = f"{base_ip[0]}.{base_ip[1]}.{base_ip[2]}.{i}"
        threading.Thread(target=ping_silencioso, args=(ip,)).start()

# Función para imprimir el resumen de dispositivos encontrados
def imprimir_resumen():
    print("\nResumen de dispositivos encontrados:")
    for ip in dispositivos_activados:
        mac = obtener_mac(ip)
        tipo = determinar_tipo_dispositivo(mac) if mac != "MAC no encontrada" else "No se pudo determinar"
        print(f"IP: {ip} | MAC: {mac} | Tipo de dispositivo: {tipo}")

# Función principal
def main():
    rango_red = "192.168.1.0/24" # Modificar en función del rango a escanear
    escanear_red(rango_red)
    time.sleep(10)  # Ajusta este tiempo dependiendo del nivel de sigiloso
    imprimir_resumen()

if __name__ == "__main__":
    main()
