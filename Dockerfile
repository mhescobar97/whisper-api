FROM ubuntu:22.04

# Instalar dependencias
RUN apt-get update && apt-get install -y \
  build-essential cmake ffmpeg git wget curl python3 python3-pip

# Clonar whisper.cpp
RUN git clone https://github.com/ggerganov/whisper.cpp.git /app
WORKDIR /app

# Compilar
RUN make

# Descargar modelo base (puedes cambiar a tiny/small/etc)
RUN ./models/download-ggml-model.sh base

# Instalar Flask para API ligera
RUN pip install flask

# Copiar script REST API (lo defines tú abajo)
COPY api.py .

# Exponer puerto
EXPOSE 5000

# Comando de inicio
CMD ["python3", "api.py"]
