import os
import logging
from datetime import datetime
import sys
import pandas as pd


# ----------------
#   
nome_programa = os.path.basename(sys.argv[0])

# ----------------
#   Diretórios
dir_data_02 = r"B:\Meus Documentos\Documentos\projetos\desafio-f360\dados\desafio_02"
dir_log = r"B:\Meus Documentos\Documentos\projetos\desafio-f360\dados\logs"

# ----------------
#   Log do maestro
agora = datetime.now()
data_log = agora.strftime("%Y-%m-%d")
arquivo_log_basename = nome_programa + '.' + data_log + '.log'
arquivo_log = os.path.join(dir_log, arquivo_log_basename)
file_handler = logging.FileHandler(arquivo_log, encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s(%(process)d)%(levelname)s %(message)s'))
logging.basicConfig(level=logging.INFO, handlers=[file_handler])
logging.info(f"Nome do programa: {nome_programa}")
