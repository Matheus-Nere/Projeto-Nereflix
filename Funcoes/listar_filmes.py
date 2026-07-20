import os
import json
pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_script, "..", "Catalogo", "lista_filmes.json")
caminho_json = os.path.abspath(caminho_json)

def listafilmes():
    with open (caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        print(json.dumps(dados, indent=4, ensure_ascii=False))
