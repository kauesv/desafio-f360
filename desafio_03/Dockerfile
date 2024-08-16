FROM python:3.12.2

# diretório
WORKDIR /desafio_03

# Copie os arquivos
COPY ./desafio_03 /desafio_03

# desabilitar o buffering, para sair no terminal
ENV PYTHONUNBUFFERED=1

# Instala as dependências
RUN pip install -r requirements.txt

# Comando para rodar o desafio e manter o container ativo
# Nele estou executando um shell no container e passo o comando tail -f /dev/null para
#impedir que o container seja finalizado
CMD sh -c "pytest testes.py && tail -f /dev/null"