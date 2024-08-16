FROM python:3.12

# Cria o Diretório de trabalho no docker
WORKDIR /desafio_01

# Copie os arquivos da pasta local para a pasta do docker
COPY ./desafio_01 /desafio_01

# Copie o arquivo .env da pasta anterior ao projeto para o container
COPY ./.env .env

# desabilitar o buffering, para sair no terminal
ENV PYTHONUNBUFFERED=1

# Instala as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando para rodar o desafio e manter o container ativo
# Nele estou executando um shell no container e passo o comando tail -f /dev/null para
#impedir que o container seja finalizado
CMD sh -c "python main.py && tail -f /dev/null"

#CMD ["ls"]
#docker exec -it 1d523f617eb4 /bin/sh