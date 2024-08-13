from cachetools import TTLCache, cached
import requests
import logging


# Configurando o cache com um Time-To-Live (TTL) de 600 segundos (10 minutos)
cache = TTLCache(maxsize=100, ttl=600)

# Visualizando o cache
# for key, value in cache.items():
#     print(f"{key}: {value}")

# ----------------
# 
@cached(cache)
def obtem_dados_openweathermap(nome, lat, long, api_key):
    """"""
    try:
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid={api_key}&lang=pt_br"

        response = requests.get(url=url)
        response_json = response.json()

        if response.status_code != 200:
            raise Exception(f"Erro na chamada da API, retorno: {response.json()}")
        else:
            logging.info(f"response returned successfully | status_code: {response.status_code}")

            kelvin = response_json['current']['temp']
            celsius = kelvin - 273.15

            result = {
                "local": nome,
                "temperatura_kelvin": kelvin,
                "temperatura_celsius": celsius,
                "umidade": response_json['current']['humidity'],
                "condicoes_do_tempo": response_json['current']['weather'][0]['description']
            }
            logging.info(f"returned data: {result}")
            return result
    except Exception as e:
        logging.error(e)
        raise


# ----------------
# 
@cached(cache)
def obtem_dados_weatherstack(cidade, api_key):
    """"""
    try:
        url = f"http://api.weatherstack.com/current?access_key={api_key}&query={cidade}"

        response = requests.get(url=url)
        response_json = response.json()

        if 'error' in response_json:
            raise Exception(f"Erro na chamada da API, retorno: {response.json()}")
        else:
            logging.info(f"response returned successfully | status_code: {response.status_code}")

            result = {
                "cidade": response_json['location']['region'],
                "temperatura": response_json['current']['temperature'],
                "umidade": response_json['current']['humidity'],
                "condicoes_do_tempo": response_json['current']['weather_descriptions'][0]
            }
            logging.info(f"returned data: {result}")
            return result
    except Exception as e:
        logging.error(e)
        raise