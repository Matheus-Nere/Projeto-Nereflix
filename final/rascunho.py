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

def menu ():
    print("NEREFLIX\n")
    print(
    "Opção 1 - Adicionar Filme\n " \
    "Opção 2 - Modificar Filme\n"  \
    "Opção 3 - Buscar Filme\n" \
    "Opção 4 - Excluir Filme\n" \
    "Opção 5 - sair\n" )

menu()
def opcao ():
    option = int(input("escolha uma opção:\n"))
    if option == 1:
        adicionarFilmes()
        print("filme adicionado")
        time.sleep(3)
        os.system("clear")
    if option == 2:
        filme = str(input("Digite o nome do filme quer deseja modificar: \n"))
        modificar_filmes(filme)
    if option == 5:
        os.system("clear")
    if option == 3:
        os.system("clear")
        buscar_filmes
opcao()