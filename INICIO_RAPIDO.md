# 🚀 Inicio Rápido - Escáner de Red

## ⚡ Setup en 5 Minutos

### 1️⃣ **Instalación Rápida**
```powershell
# Clonar proyecto
git clone https://github.com/margandona/escaneo.git
cd escaneo

# Instalar Nmap
winget install "Nmap"

# Instalar dependencias Python
pip install python-nmap
```

### 2️⃣ **Primera Prueba**
```powershell
# Probar con localhost
python scan_subnet.py 127.0.0.1/32
```

### 3️⃣ **Escaneos Comunes**
```powershell
# Tu router/gateway
python scan_subnet.py 192.168.1.1/32

# Escaneo rápido (16 IPs)
python scan_subnet.py 192.168.1.0/28

# Escaneo completo (254 IPs)
python scan_subnet.py 192.168.1.0/24
```

## 🎯 **Comandos por Situación**

| Situación | Comando | Tiempo |
|-----------|---------|--------|
| **Primera prueba** | `python scan_subnet.py 127.0.0.1/32` | 30s |
| **Router/Gateway** | `python scan_subnet.py 192.168.1.1/32` | 1min |
| **Escaneo rápido** | `python scan_subnet.py 192.168.1.0/28` | 2-3min |
| **Red completa** | `python scan_subnet.py 192.168.1.0/24` | 10-15min |
| **Red corporativa** | `python scan_subnet.py 10.0.0.0/24` | 10-15min |

## 🔧 **Solución Rápida de Problemas**

### ❌ **"Nmap no encontrado"**
```powershell
& "C:\Program Files (x86)\Nmap\nmap.exe" --version
```

### ❌ **"No se puede acceder a la red"**
```powershell
# Verificar tu IP
ipconfig | findstr "IPv4"

# Verificar conectividad
ping 192.168.1.1
```

### ❌ **Muy lento**
```powershell
# Usar rangos más pequeños
python scan_subnet.py 192.168.1.0/28  # Solo 16 IPs
```

## 📖 **Leer Resultados**

```
Host: 192.168.1.1
  Puertos abiertos:
    - Puerto 22/tcp: ssh | Versión: OpenSSH 7.4      ← Acceso SSH
    - Puerto 53/tcp: domain | Versión: dnsmasq 2.80  ← Servidor DNS
    - Puerto 80/tcp: http | Versión: nginx 1.18.0    ← Servidor Web
```

## ⚠️ **Importante**
- ✅ Solo usar en **redes propias**
- ✅ Obtener **autorización** antes de escanear
- ✅ Para **auditorías éticas** únicamente

---
📚 **Manual completo:** `GUIA_DE_USO.md`
