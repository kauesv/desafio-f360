FROM python:3.12.2

# diretório
WORKDIR /desafio_03

# Copie os arquivos
COPY ./desafio_03 /desafio_03

# desabilitar o buffering, para sair no terminal
ENV PYTHONUNBUFFERED=1

# Instala as dependências
RUN pip install -r requirements.txt

# Comando para rodar o desafio
CMD ["pytest", "testes.py"]