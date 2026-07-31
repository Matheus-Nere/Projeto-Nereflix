import os
import json
import time
pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_script, "..", "Catalogo", "lista_filmes.json")
caminho_json = os.path.abspath(caminho_json)

def listar ():
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        print(dados)
        saida = input("\npressione qualquer tecla para sair.")
        



def buscar ():
    filme = str(input("\nDigite o nome do filme que deseja encontrar: \n"))
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        for i in dados:
            if i['nome'].lower() == filme.lower():
               
                print(i)
                saida = input("\npressione qualquer tecla para sair.")
                if saida:
                    buscar_filmes()
                
def sair ():
    print()
    print("Opção invalida, digite o numero referente a opção escolhida.")
    time.sleep(1)
    buscar_filmes ()

def buscar_filmes ():
    print()
    opcao = str(input(
    "1 - Listar todos os filmes\n\n" \
    "2 - Buscar um filme especifico\n\n" \
    "3 - Sair\n\n" \
    "Escolha uma das opções:\n\n" ))
    if opcao == "1":
        listar ()
    if opcao == "2":
        buscar ()
    else:
        sair()
    buscar_filmes()
    
buscar_filmes ()
