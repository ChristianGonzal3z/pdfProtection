LABEL authors="Christian Gonzalez"
# Imagen base de Python
FROM python:3.9-slim
# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Iniciar la aplicación
CMD ["python", "app.py"]