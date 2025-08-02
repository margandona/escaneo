# Escáner de Subred con Nmap

## 📋 Descripción

Script de Python para escaneo de redes utilizando Nmap y python-nmap. Diseñado para auditorías éticas de ciberseguridad en entornos controlados.

## ⚠️ Advertencia Legal

**USO ÉTICO ÚNICAMENTE**: Este script está diseñado exclusivamente para:
- Auditorías de seguridad autorizadas
- Pruebas en entornos propios o controlados
- Fines educativos y de aprendizaje

**NO** utilizar en redes sin autorización explícita. El uso indebido puede constituir una actividad ilegal.

## 🚀 Características

- ✅ Escaneo completo de subredes (ejemplo: 192.168.1.0/24)
- ✅ Detección de hosts activos
- ✅ Identificación de puertos abiertos
- ✅ Detección de servicios y versiones (-sV)
- ✅ Validación de errores y dependencias
- ✅ Informes organizados para análisis técnico
- ✅ Resumen estadístico del escaneo

## 📦 Requisitos

### Software necesario:
- **Python 3.6+**
- **Nmap** (instalado en el sistema)
- **python-nmap** (librería de Python)

### Instalación de dependencias:

```bash
# Instalar Nmap en Windows
# Descargar desde: https://nmap.org/download.html

# Instalar python-nmap
pip install python-nmap
```

## 🛠️ Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/margandona/escaneo.git
cd escaneo
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Verificar instalación de Nmap:**
```bash
nmap --version
```

## 📖 Uso

### Escaneo básico (subred por defecto):
```bash
python scan_subnet.py
```

### Escaneo de subred específica:
```bash
python scan_subnet.py 192.168.1.0/24
```

### Ejemplos de subredes:
```bash
# Red local típica
python scan_subnet.py 192.168.1.0/24

# Red corporativa
python scan_subnet.py 10.0.0.0/24

# Red específica
python scan_subnet.py 172.16.1.0/24
```

## 📊 Salida del Script

El script genera un informe detallado que incluye:

```
[INFO] Iniciando escaneo en la subred 192.168.1.0/24 (esto puede tardar)...
[INFO] Hosts activos encontrados: 3

Host: 192.168.1.1
  Puertos abiertos:
    - Puerto 22/tcp: ssh | Versión: OpenSSH 8.2
    - Puerto 80/tcp: http | Versión: Apache 2.4.41
    - Puerto 443/tcp: https | Versión: Apache 2.4.41
--------------------------------------------------
Host: 192.168.1.100
  Puertos abiertos:
    - Puerto 135/tcp: msrpc | Versión: Microsoft Windows RPC
    - Puerto 445/tcp: microsoft-ds | Versión: No detectada
--------------------------------------------------

[RESUMEN] Total de hosts escaneados: 254
[RESUMEN] Total de hosts activos: 3
```

## 🔧 Estructura del Código

```
escaneo/
├── scan_subnet.py      # Script principal
├── README.md          # Documentación
└── requirements.txt   # Dependencias
```

### Funciones principales:

- `check_nmap_installed()`: Valida si Nmap está instalado
- `check_network_accessible()`: Verifica accesibilidad de la red
- `scan_subnet()`: Función principal de escaneo

## 🛡️ Consideraciones de Seguridad

1. **Autorización**: Obtén autorización explícita antes de escanear cualquier red
2. **Entornos controlados**: Usa únicamente en redes propias o de prueba
3. **Registros**: Los escaneos pueden generar logs en sistemas objetivo
4. **Impacto**: Los escaneos intensivos pueden afectar el rendimiento de la red

## 🔍 Solución de Problemas

### Error: "Nmap no está instalado"
```bash
# Windows: Descargar e instalar desde https://nmap.org/download.html
# Linux: sudo apt install nmap
# macOS: brew install nmap
```

### Error: "No se puede acceder a la red objetivo"
- Verificar conectividad de red
- Comprobar que la subred especificada sea válida
- Verificar permisos de red/firewall

### Error: "Permission denied"
- En Linux/macOS: ejecutar con `sudo` si es necesario
- Verificar permisos de usuario

## 📚 Documentación Adicional

- [Documentación oficial de Nmap](https://nmap.org/docs.html)
- [Python-nmap documentation](https://python-nmap.readthedocs.io/)
- [Guía de escaneo ético](https://nmap.org/book/legal-issues.html)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## ⚖️ Descargo de Responsabilidad

El autor no se hace responsable del uso indebido de esta herramienta. Es responsabilidad del usuario asegurar que su uso cumple con todas las leyes y regulaciones aplicables.

---

**Desarrollado con fines educativos y de auditoría ética** 🛡️
