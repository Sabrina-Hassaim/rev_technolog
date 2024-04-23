FROM python:3.10

# Install
WORKDIR /app
RUN pip install uvicorn fastapi pymongo pydantic typing

# Copiez le code de l'application dans le conteneur
COPY . .

# Démarrez l'app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]