import json
import os

def adicionarFilmes ():
    filme = {"nome": 0, "diretor": 0, "genero": 0, "ano": 0}
    fnome = input("insira o nome do filme:\n")
    fdiretor = input("Insira o nome do diretor do filme:\n")
    fgenero = input("Insira o genero do filme:\n")
    fano = input("Insira o ano de criação do filme:\n")
    filme["nome"] = fnome
    filme["diretor"] = fdiretor
    filme["genero"] = fgenero
    filme["ano"] = fano
    if os.path.exists("Catalogo.lista_filmes.json"):
     with open("Catalogo.lista_filmes.json", "r", encoding="utf-8") as filme:
        dados_existentes = json.load(filme)
    else:
        dados_existentes = {}

    dados_existentes.update(filme)

    with open("Catalogo.lista_filmes.json", "w", encoding="utf-8") as filme:
        json.dump(dados_existentes, filme, ensure_ascii=False, indent=4)

adicionarFilmes()

#import Funções.adicionar_filmes as adicionar_filmes