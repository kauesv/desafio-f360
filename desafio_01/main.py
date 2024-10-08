import requests
from dotenv import load_dotenv
import os
import json
import logging
from datetime import datetime
import sys
from api import obtem_dados_openweathermap, obtem_dados_weatherstack


# ----------------
#   
nome_programa = os.path.basename(sys.argv[0])

# ----------------
#   Diretórios
dir_data_01 = r"dados"
dir_log = r"dados/logs"

# ----------------
#   Log
agora = datetime.now()
data_log = agora.strftime("%Y-%m-%d")
arquivo_log_basename = nome_programa + '.' + data_log + '.log'
arquivo_log = os.path.join(dir_log, arquivo_log_basename)
file_handler = logging.FileHandler(arquivo_log, encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s(%(process)d)%(levelname)s %(message)s'))
logging.basicConfig(level=logging.INFO, handlers=[file_handler])
logging.info(f"Nome do programa: {nome_programa}")

# ----------------
#   Carrega arquivo .env
load_dotenv()

# ----------------
#   Variaveis
api_key_openweathermap = os.getenv('APIKEY_1')
api_key_weatherstack = os.getenv('APIKEY_2')

# ----------------
#   Obtem coordenadas do arquivo json
arquivo_json = dir_data_01 + "/coordenadas.json"
logging.info(f"arquivo JSON: {arquivo_json}")
try:
    with open(arquivo_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
except:
    logging.error("ERRO:", exc_info=True)
    raise

# ----------------
#   Resultado openweathermap
logging.info(f"Executando Openweathermap")
list_result = []
for coord in data:
    nome = coord['nome']
    lat = coord['lat']
    long = coord['long']
    logging.info(f"Coordenadas: {coord}")

    try:
        result = obtem_dados_openweathermap(nome, lat, long, api_key_openweathermap)
        print("Openweathermap")
        print(json.dumps(result, indent=4, ensure_ascii=False))

        list_result.append(result)
    except:
        print('Houve um erro no openweathermap')

#print(list_result)

# ----------------
#   Resultado weatherstack
logging.info(f"Executando Weatherstack")
try:
    result = obtem_dados_weatherstack("Sao Paulo", api_key_weatherstack)
    print("Weatherstack")
    print(json.dumps(result, indent=4, ensure_ascii=False))
except:
    print('Houve um erro no weatherstack')