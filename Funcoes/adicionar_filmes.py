import json
import os

pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_script, "..", "Catalogo", "lista_filmes.json")
caminho_json = os.path.abspath(caminho_json)

def adicionarFilmes():
    novo_filme = {"nome": 0, "diretor": 0, "genero": 0, "ano": 0}
    fnome = input("insira o nome do filme:\n")
    fdiretor = input("Insira o nome do diretor do filme:\n")
    fgenero = input("Insira o genero do filme:\n")
    fano = input("Insira o ano de criação do filme:\n")
    novo_filme["nome"] = fnome
    novo_filme["diretor"] = fdiretor
    novo_filme["genero"] = fgenero
    novo_filme["ano"] = fano


    if os.path.exists(caminho_json) and os.path.getsize(caminho_json) > 0:
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            dados_existentes = json.load(arquivo)
    else:
        dados_existentes = []

    dados_existentes.append(novo_filme)

    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)