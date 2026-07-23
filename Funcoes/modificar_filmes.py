import os
import json
pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_script, "..", "Catalogo", "lista_filmes.json")
caminho_json = os.path.abspath(caminho_json)

def listafilmes(filme):
    with open (caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        for i in dados:
            if i['nome'] == filme:
                print (i)
                print()
                opcao = input("Filme econtrado, escolha a informação para modificar")
                if opcao == "nome":
                    print()
                if opcao == "diretor":
                    print()
                if opcao == "genero":
                    print()
                if opcao == "ano":
                    print()
                else:
                    print("Opção não encontrada, tente novamente")
        print("filme não encontrado")

