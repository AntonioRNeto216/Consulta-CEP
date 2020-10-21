import requests
from typing import Tuple

def abre_url(cep: str) -> Tuple[dict, int]:
    retorno = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
    status_code = retorno.status_code
    if status_code == 200:
        dados_cep = retorno.json()
        return dados_cep, status_code
    else:
        return {}, status_code