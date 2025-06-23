# Whisper.cpp REST API (Dokploy ready)

Este proyecto expone Whisper.cpp como un servicio REST para transcribir audio a texto, ideal para integraciones con n8n, WhatsApp bots, etc.

### ✅ Requisitos

- Docker
- Cuenta en [Dokploy](https://dokploy.com)

### 🚀 Uso local

```bash
docker build -t whisper-api .
docker run -p 5000:5000 whisper-api
```
