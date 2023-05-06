# PDF Protection
Esta es una aplicación Flask simple que te permite proteger archivos PDF con una contraseña. Al enviar un archivo PDF y una contraseña a través de un formulario web, la aplicación generará un nuevo archivo PDF protegido con la contraseña especificada.

Esta es una aplicación Flask simple que te permite proteger archivos PDF con una contraseña. Al enviar un archivo PDF y una contraseña a través de un formulario web, la aplicación generará un nuevo archivo PDF protegido con la contraseña especificada.

### Instalación
Clona este repositorio:
```bash
git clone https://github.com/ChristianGonzal3z/pdfProtection.git
```
Instala los paquetes necesarios:
```bash
pip install -r requirements.txt
```
Ejecuta la aplicación:
```bash
python app.py
```
Abre un navegador web y navega a http://localhost:5000.

Selecciona un archivo PDF y escribe una contraseña.

Haz clic en el botón "Proteger" y la aplicación generará un nuevo archivo PDF protegido con la contraseña especificada.
### Docker

1. Navega al directorio de la aplicación: 

```bash
  cd pdfProtection
```
2. Construye la imagen de Docker a partir del Dockerfile:

```bash
  docker build -t pdfProtection .
```
3. Inicia un contenedor a partir de la imagen de Docker:

```bash
  docker run -p 5000:5000 pdfProtection
```

## Licencia
Esta aplicación está bajo la Licencia MIT. Si deseas obtener más información, lee el archivo LICENSE. 