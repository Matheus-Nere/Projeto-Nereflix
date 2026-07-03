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
    return filme
import Funções.adicionar_filmes as adicionar_filmes