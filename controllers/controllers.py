from models.models import Endereco
import requests
import json

def format_cep(cep):
    return f"{cep[:5]}-{cep[5:]}"

def search_endereco_by_cep(cep):
    url = f'https://viacep.com.br/ws/%7Bcep%7D/json/'
    response = requests.get(url)

    if response.status_code == 200 and response.text.strip():
        try:
            data = response.json()
            if 'erro' not in data:
                formatted_cep = format_cep(data.get('cep', ''))
                endereco = endereco(
                    id=1,
                    endereco=data.get('logradouro', ''),
                    bairro=data.get('bairro', ''),
                    cidade=data.get('localidade', ''),
                    uf=data.get('uf', ''),
                    cep=formatted_cep
                )
                return [endereco]
        except json.JSONDecodeError as e:
            print(f"Erro de decodificação JSON: {e}")
            pass

    return []