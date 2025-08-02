# 🔍 Guía de Uso del Escáner de Red con Nmap

## 📋 Tabla de Contenidos
1. [Prerrequisitos](#prerrequisitos)
2. [Instalación](#instalación)
3. [Configuración del Entorno](#configuración-del-entorno)
4. [Primeros Pasos](#primeros-pasos)
5. [Ejemplos de Uso](#ejemplos-de-uso)
6. [Interpretación de Resultados](#interpretación-de-resultados)
7. [Troubleshooting](#troubleshooting)
8. [Mejores Prácticas](#mejores-prácticas)

---

## 📦 Prerrequisitos

### Software Necesario:
- ✅ **Windows 10/11** (o Linux/macOS)
- ✅ **Python 3.6 o superior**
- ✅ **Nmap** (herramienta de escaneo de red)
- ✅ **Librería python-nmap**

### Verificaciones Iniciales:

```powershell
# Verificar Python
python --version

# Verificar si tienes permisos de administrador
whoami /groups | findstr "S-1-5-32-544"
```

---

## 🚀 Instalación

### Paso 1: Descargar el Proyecto

```bash
# Clonar desde GitHub
git clone https://github.com/margandona/escaneo.git
cd escaneo
```

### Paso 2: Instalar Nmap

#### En Windows:
```powershell
# Opción 1: Usando winget (recomendado)
winget install "Nmap"

# Opción 2: Descarga manual
# Ir a: https://nmap.org/download.html
# Descargar e instalar el .exe
```

#### En Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install nmap
```

#### En macOS:
```bash
# Con Homebrew
brew install nmap
```

### Paso 3: Verificar Instalación de Nmap

```powershell
# Windows - Verificar con ruta completa
& "C:\Program Files (x86)\Nmap\nmap.exe" --version

# Linux/macOS
nmap --version
```

### Paso 4: Configurar Python y Dependencias

```powershell
# Configurar entorno Python (automático en VS Code)
# El script configurará automáticamente el entorno

# Instalar dependencias
pip install python-nmap
```

---

## ⚙️ Configuración del Entorno

### Verificar tu Red Local:

```powershell
# Ver tu IP actual
ipconfig | findstr "IPv4"

# Ejemplo de salida:
# Dirección IPv4. . . . . . . . . . . . . . : 192.168.1.100
```

### Identificar tu Subred:
- Si tu IP es `192.168.1.100`, tu subred es `192.168.1.0/24`
- Si tu IP es `10.0.0.50`, tu subred es `10.0.0.0/24`
- Si tu IP es `172.16.1.25`, tu subred es `172.16.1.0/24`

---

## 🎯 Primeros Pasos

### 1. Prueba Básica (Localhost)

```powershell
# Probar el script con tu propia máquina
python scan_subnet.py 127.0.0.1/32
```

**Resultado esperado:**
```
[INFO] Nmap encontrado en: C:\Program Files (x86)\Nmap\nmap.exe
[INFO] Iniciando escaneo en la subred 127.0.0.1/32 (esto puede tardar)...
[INFO] Hosts activos encontrados: 1

Host: 127.0.0.1
  Puertos abiertos:
    - Puerto 135/tcp: msrpc | Versión: Microsoft Windows RPC
    - Puerto 445/tcp: microsoft-ds | Versión: No detectada
```

### 2. Escanear el Gateway (Router)

```powershell
# Escanear tu router/gateway (usualmente .1)
python scan_subnet.py 192.168.1.1/32
```

### 3. Escaneo de Subred Pequeña

```powershell
# Escanear solo 16 direcciones (más rápido)
python scan_subnet.py 192.168.1.0/28
```

---

## 💡 Ejemplos de Uso

### Escaneos por Alcance:

#### 🔹 **Escaneo Rápido** (4 IPs - 30 segundos):
```powershell
python scan_subnet.py 192.168.1.1/30
```

#### 🔹 **Escaneo Medio** (16 IPs - 2-3 minutos):
```powershell
python scan_subnet.py 192.168.1.0/28
```

#### 🔹 **Escaneo Completo** (254 IPs - 10-15 minutos):
```powershell
python scan_subnet.py 192.168.1.0/24
```

### Escaneos por Tipo de Red:

#### 🏠 **Red Doméstica Típica:**
```powershell
python scan_subnet.py 192.168.1.0/24
python scan_subnet.py 192.168.0.0/24
```

#### 🏢 **Red Corporativa:**
```powershell
python scan_subnet.py 10.0.0.0/24
python scan_subnet.py 172.16.1.0/24
```

#### 🔬 **Red de Laboratorio:**
```powershell
python scan_subnet.py 192.168.56.0/24  # VirtualBox
python scan_subnet.py 192.168.100.0/24  # VMware
```

### Escaneos Específicos:

#### 📱 **Solo Dispositivos Móviles** (rango típico):
```powershell
python scan_subnet.py 192.168.1.100/28
```

#### 🖥️ **Solo Servidores** (rango típico):
```powershell
python scan_subnet.py 192.168.1.10/29
```

---

## 📊 Interpretación de Resultados

### Ejemplo de Salida Completa:

```
[INFO] Nmap encontrado en: C:\Program Files (x86)\Nmap\nmap.exe
[INFO] Iniciando escaneo en la subred 192.168.1.0/24 (esto puede tardar)...
[INFO] Hosts activos encontrados: 5

Host: 192.168.1.1
  Puertos abiertos:
    - Puerto 22/tcp: ssh | Versión: OpenSSH 7.4
    - Puerto 53/tcp: domain | Versión: dnsmasq 2.80
    - Puerto 80/tcp: http | Versión: nginx 1.18.0
    - Puerto 443/tcp: https | Versión: nginx 1.18.0
--------------------------------------------------
Host: 192.168.1.10
  Puertos abiertos:
    - Puerto 22/tcp: ssh | Versión: OpenSSH 8.2
    - Puerto 3306/tcp: mysql | Versión: MySQL 8.0.25
--------------------------------------------------
Host: 192.168.1.15
  Puertos abiertos:
    - Puerto 80/tcp: http | Versión: Apache 2.4.41
    - Puerto 443/tcp: https | Versión: Apache 2.4.41
--------------------------------------------------

[RESUMEN] Total de hosts escaneados: 254
[RESUMEN] Total de hosts activos: 5
```

### 🔍 **Análisis de la Información:**

#### **192.168.1.1 (Router/Gateway):**
- **SSH (22)**: Acceso remoto seguro
- **DNS (53)**: Servidor DNS local
- **HTTP/HTTPS (80/443)**: Interfaz web de administración

#### **192.168.1.10 (Servidor de Base de Datos):**
- **SSH (22)**: Acceso administrativo
- **MySQL (3306)**: Base de datos expuesta ⚠️

#### **192.168.1.15 (Servidor Web):**
- **HTTP/HTTPS (80/443)**: Servidor web público

---

## 🛠️ Troubleshooting

### ❌ **Error: "Nmap no está instalado"**

**Solución:**
```powershell
# Reinstalar Nmap
winget uninstall "Nmap"
winget install "Nmap"

# Verificar instalación
& "C:\Program Files (x86)\Nmap\nmap.exe" --version
```

### ❌ **Error: "No se puede acceder a la red objetivo"**

**Posibles causas:**
1. **Red incorrecta**: Verifica tu IP con `ipconfig`
2. **Firewall**: Temporalmente desactiva Windows Defender
3. **VPN activa**: Desconecta VPN temporalmente

**Solución:**
```powershell
# Verificar conectividad
ping 192.168.1.1

# Verificar tu red actual
ipconfig | findstr "IPv4"
```

### ❌ **Error: "Permission denied"**

**Solución:**
```powershell
# Ejecutar como administrador
# Clic derecho en PowerShell > "Ejecutar como administrador"
```

### ❌ **Escaneo muy lento**

**Optimizaciones:**
```powershell
# Usar rangos más pequeños
python scan_subnet.py 192.168.1.0/28  # 16 IPs en lugar de 254

# Escanear solo dispositivos conocidos
python scan_subnet.py 192.168.1.1/32   # Solo el router
python scan_subnet.py 192.168.1.100/30 # Solo 4 IPs
```

---

## 🔒 Mejores Prácticas

### ⚖️ **Uso Ético:**
1. ✅ **Solo en redes propias** o con autorización explícita
2. ✅ **Documentar todos los escaneos** realizados
3. ✅ **Horarios apropiados** (evitar horas pico)
4. ✅ **Informar hallazgos** a los responsables de seguridad

### 🕐 **Horarios Recomendados:**
- **Entorno corporativo**: Fuera del horario laboral
- **Red doméstica**: Cualquier momento
- **Laboratorios**: Según políticas del centro

### 📝 **Documentación:**
```powershell
# Guardar resultados en archivo
python scan_subnet.py 192.168.1.0/24 > scan_results_$(Get-Date -Format "yyyy-MM-dd_HH-mm").txt
```

### 🔍 **Progresión Recomendada:**

#### **Principiante:**
1. Localhost (`127.0.0.1/32`)
2. Gateway (`192.168.1.1/32`)
3. Rango pequeño (`192.168.1.0/28`)

#### **Intermedio:**
1. Subred completa (`192.168.1.0/24`)
2. Múltiples subredes
3. Análisis de servicios específicos

#### **Avanzado:**
1. Redes corporativas grandes
2. Integración con otras herramientas
3. Automatización y reportes

---

## 📞 Soporte

### 🆘 **Si encuentras problemas:**

1. **Revisa este manual** completo
2. **Verifica prerrequisitos** uno por uno
3. **Prueba con localhost** primero
4. **Consulta logs** de error específicos

### 📚 **Recursos Adicionales:**
- [Documentación oficial Nmap](https://nmap.org/docs.html)
- [Guía de python-nmap](https://python-nmap.readthedocs.io/)
- [Repositorio del proyecto](https://github.com/margandona/escaneo)

---

**⚠️ Recuerda: Este script es para auditorías éticas únicamente. Úsalo responsablemente.** 🛡️
