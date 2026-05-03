# 🕸️ Network Scanner

**Escáner de red sigiloso con identificación de dispositivos por MAC**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey?style=flat-square&logo=linux)
![License](https://img.shields.io/badge/Use-Ethical%20Hacking%20Only-red?style=flat-square)
![Author](https://img.shields.io/badge/creator-hug0x-sec-cyan?style=flat-square)

---

## ¿Qué hace?

Escanea un rango de IPs de tu red local mediante ping sigiloso multihilo, identifica los dispositivos activos y para cada uno obtiene su dirección MAC e intenta determinar el tipo de dispositivo (móvil, PC, desconocido) consultando el fabricante a través del prefijo OUI de la MAC.

---

## ⚡ Funcionamiento

| Fase | Qué hace |
|------|----------|
| 1. Ping sigiloso | Lanza un ping a cada IP del rango en un hilo independiente |
| 2. Detección de activos | Registra las IPs que responden |
| 3. Obtención de MAC | Consulta la tabla ARP del sistema para cada IP activa |
| 4. Identificación del fabricante | Usa el prefijo OUI de la MAC para determinar el fabricante |
| 5. Clasificación del dispositivo | Clasifica el dispositivo como Móvil, PC o Desconocido |
| 6. Resumen final | Imprime una tabla con IP, MAC y tipo de cada dispositivo encontrado |

---

## 🖥️ Compatibilidad

| Sistema | Soporte |
|---------|---------|
| Linux / macOS | ✅ |
| Windows | ✅ |

El script detecta automáticamente el sistema operativo y ajusta los comandos de `ping` y `arp` en consecuencia.

---

## 🛠️ Requisitos

- Python 3.8+
- Librería `mac-vendor-lookup`

---

## 📥 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/hug0x-sec/pentest-toolkit
cd network-scanner

# Instalar dependencias
pip install mac-vendor-lookup
```

O descargar solo el script:

```bash
wget https://raw.githubusercontent.com/hug0x-sec
pip install mac-vendor-lookup
```

---

## ⚙️ Configuración

Antes de ejecutar, edita la línea del rango de red en `main()` para que coincida con tu red local:

```python
rango_red = "192.168.1.0/24"   # <-- cámbialo por tu rango
```

Ejemplos de rangos habituales:

| Red | Rango |
|-----|-------|
| Router doméstico | `192.168.1.0/24` |
| Router alternativo | `192.168.0.0/24` |
| VPN / Lab | `10.10.10.0/24` |

También puedes ajustar el tiempo de espera entre el escaneo y el resumen final (por defecto 10 segundos):

```python
time.sleep(10)   # auméntalo si la red es lenta o el rango es grande
```

---

## 🚀 Uso

```bash
python3 scanner.py
```

---

## 🖥️ Ejemplo de salida

```
Escaneando el rango 192.168.1.0/24 para encontrar dispositivos activos...

Dispositivo activo encontrado: 192.168.1.1
Dispositivo activo encontrado: 192.168.1.35
Dispositivo activo encontrado: 192.168.1.102

Resumen de dispositivos encontrados:
IP: 192.168.1.1   | MAC: A4:B1:C2:D3:E4:F5 | Tipo de dispositivo: Dispositivo desconocido
IP: 192.168.1.35  | MAC: 3C:22:FB:AA:11:CC  | Tipo de dispositivo: Móvil
IP: 192.168.1.102 | MAC: 00:1A:2B:3C:4D:5E  | Tipo de dispositivo: PC
```

---

## 📦 Dependencias

| Librería | Uso | Instalación |
|----------|-----|-------------|
| `mac-vendor-lookup` | Identificar fabricante por MAC | `pip install mac-vendor-lookup` |
| `subprocess` | Ejecutar ping y arp | Estándar de Python |
| `threading` | Escaneo paralelo de IPs | Estándar de Python |
| `socket` | Utilidades de red | Estándar de Python |
| `platform` | Detectar el SO | Estándar de Python |
| `re` | Extraer MAC con regex | Estándar de Python |

---

## ⚠️ Aviso legal

Esta herramienta está diseñada **exclusivamente para analizar redes sobre las que tienes autorización expresa**. Escanear redes ajenas sin permiso es ilegal. El autor no se responsabiliza del mal uso de esta herramienta.

---

<div align="center">
  Hecho con ☕ por <strong>hug0x-sec</strong>
</div>
