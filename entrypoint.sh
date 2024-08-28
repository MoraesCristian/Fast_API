#!/bin/sh

#Executa as migracoes do bando de dados
poetry run alembic upgrade head

#inicia a aplicação 
#poetry run uvicorn --host 0.0.0.0 --port 8000 fast_api.app:app
exec poetry run fastapi run fast_api/app.py --host 0.0.0.0