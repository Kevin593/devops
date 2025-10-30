# Imagen base oficial de Python
FROM python:3.14-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de requerimientos y código
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto en el que correrá Flask
EXPOSE 8080

# Comando para ejecutar la app
CMD ["python", "app.py"]
