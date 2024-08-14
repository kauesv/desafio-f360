FROM jupyter/base-notebook:python-3.9

# diretório
WORKDIR /desafio_02

# Copie os arquivos da pasta local para a pasta do docker
COPY ./desafio_02 /desafio_02

# Instala as dependências
RUN pip install -r requirements.txt

# Comando padrão para iniciar o Jupyter Notebook
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]