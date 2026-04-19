# Image de base légère
FROM python:3.12-slim

# Dossier de travail dans le container
WORKDIR /app

# Copie et installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY app.py .

# Port exposé
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]