from Funcoes.adicionar_filmes import adicionarFilmes
print("NEREFLIX\n")

print(
"Opção 1 - Adicionar Filme:\n " \
"Opção 2 - Modificar Filme:\n"  \
"Opção 3 - Buscar Filme:\n" \
"Opção 4 - Excluir Filme:\n" \
"Opção 3 - Buscar Filme:\n" )

option = int(input("escolha uma opção:\n"))

if option == 1:
    adicionarFilmes()