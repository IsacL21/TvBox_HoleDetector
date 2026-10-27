# Usa uma base Debian leve com Python 3.10
FROM python:3.10-slim

WORKDIR /app

# Instala dependência do sistema que o OpenCV precisa
RUN apt-get update && apt-get install -y libglib2.0-0 && rm -rf /var/lib/apt/lists/*

# Copia e instala as bibliotecas Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o seu script e o arquivo XML do modelo
COPY . .

# Executa o código
CMD ["python", "hole2.py"]