import os
import json
pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_script, "..", "Catalogo", "lista_filmes.json")
caminho_json = os.path.abspath(caminho_json)

def modificar_filmes(filme):
    with open (caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        for i in dados:
            if i['nome'].lower() == filme.lower():
                print()
                print (i)
                print("\nfilme encontrado, iniciando modificações, mantenha em branco caso queira manter a informação.\n")
                for chave in i:
                    novo_valor = str(input(f"Insira o novo {chave} do filme: \n"))
                    i[chave] = novo_valor
                break
            else: 
                print("filme não encontrado")

                

modificar_filmes('mari')