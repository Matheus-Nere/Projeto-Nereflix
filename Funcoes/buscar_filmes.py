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
        buscar_filmes()
        

def achar (dados, filme):
    
    for i in dados:
        if i['nome'].lower() == filme.lower():
           
            filme_achado = i
            return filme_achado



def buscar ():
    filme = str(input("\nDigite o nome do filme que deseja encontrar: \n"))
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        filme_achado = achar(dados, filme)
        if filme_achado and filme_achado["nome"].lower() == filme.lower():
            print(filme_achado)
            sair = input("\npressione qualquer tecla para sair.")
        else:
            print('Filme não encontrado')
            time.sleep(1)
            buscar_filmes()

                
def opcao_errada ():
    print()
    print("Opção invalida, digite o numero referente a opção escolhida.")
    time.sleep(1)
    buscar_filmes ()

def sair ():
    print()
def buscar_filmes ():
    print()
    opcao = None
    opcao = str(input(
    "1 - Listar todos os filmes\n\n" \
    "2 - Buscar um filme especifico\n\n" \
    "3 - Sair\n\n" \
    "Escolha uma das opções:\n\n" ))
    if opcao == "1":
        listar ()
    elif opcao == "2":
        buscar ()
    elif opcao == "3":
        sair()
    else:
        opcao_errada()
    
    

