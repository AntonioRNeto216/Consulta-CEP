import requests

def abre_url(cep):
    retorno = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
    status_code = retorno.status_code
    dados_cep = retorno.json()
    return dados_cep, status_code