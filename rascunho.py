import os
import time
from Funcoes.adicionar_filmes import adicionarFilmes

def menu ():
    print("NEREFLIX\n")
    print(
    "Opção 1 - Adicionar Filme\n " \
    "Opção 2 - Modificar Filme\n"  \
    "Opção 3 - Buscar Filme\n" \
    "Opção 4 - Excluir Filme\n" \
    "Opção 5 - sair\n" )

menu()
option = int(input("escolha uma opção:\n"))

if option == 1:
    adicionarFilmes()
    print("filme adicionado")
    time.sleep(3)
    os.system("clear")

if option == 5:
    os.system("clear")