import os
import time
import sys
pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_script, "..", "Catalogo", "lista_filmes.json")
caminho_json = os.path.abspath(caminho_json)
raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(raiz_projeto)
from Funcoes.adicionar_filmes import adicionarFilmes
from Funcoes.modificar_filmes import modificar_filmes
from Funcoes.buscar_filmes import buscar_filmes
from Funcoes.excluir_filmes import excluir_filme

def opcao ():
    print()
    option = int(input("escolha uma opção:\n"))
    match option:
        case 1:
            os.system("clear")
            adicionarFilmes()
            print("filme adicionado")
            time.sleep(3)
            os.system("clear")
            menu()
        case 2:
            os.system("clear")
            filme = str(input("Digite o nome do filme quer deseja modificar: \n"))
            modificar_filmes(filme)
            os.system("clear")
            menu()
        case 3:
            os.system("clear")
            buscar_filmes()
            os.system("clear")
            menu()
        case 4:
            os.system("clear")
            filme = str(input("Digite o nome do filme quer deseja excluir: \n"))
            excluir_filme(filme)
            os.system("clear")
            menu()
        case 5:
          os.system("clear")

        
        

def menu ():
    print ("""
    ╔═╗─╔╦═══╦═══╦═══╦═══╦╗──╔══╦═╗╔═╗
    ║║╚╗║║╔══╣╔═╗║╔══╣╔══╣║──╚╣╠╩╗╚╝╔╝
    ║╔╗╚╝║╚══╣╚═╝║╚══╣╚══╣║───║║─╚╗╔╝
    ║║╚╗║║╔══╣╔╗╔╣╔══╣╔══╣║─╔╗║║─╔╝╚╗
    ║║─║║║╚══╣║║╚╣╚══╣║──║╚═╝╠╣╠╦╝╔╗╚╗
    ╚╝─╚═╩═══╩╝╚═╩═══╩╝──╚═══╩══╩═╝╚═╝""")
    print("""
    Opção 1 - Adicionar Filme
    Opção 2 - Modificar Filme
    Opção 3 - Buscar Filme
    Opção 4 - Excluir Filme
    Opção 5 - sair""")
    opcao()

menu()