import os
import time
from Funcoes.adicionar_filmes import adicionarFilmes
from Funcoes.modificar_filmes import modificar_filmes

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
        
        time.sleep(5)
        os.system("clear")
opcao()