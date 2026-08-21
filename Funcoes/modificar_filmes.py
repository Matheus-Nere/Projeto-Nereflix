import os
import json
import time
pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_script, "..", "Catalogo", "lista_filmes.json")
caminho_json = os.path.abspath(caminho_json)
def achar (dados, filme):
    
    for i in dados:
        if i['nome'].lower() == filme.lower():
           
            filme_achado = i
            return filme_achado
            
        
def modificar(i):
    print()
    print (i)
    print("\nfilme encontrado, iniciando modificações, mantenha em branco caso queira manter a informação.\n")
    for chave in i:
        novo_valor = str(input(f"Insira o novo {chave} do filme: \n"))
        if novo_valor:
            i[chave] = novo_valor
       

def modificar_filmes(filme):
    with open (caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        
        filme_achado = achar(dados, filme)
        if filme_achado and filme_achado["nome"].lower() == filme.lower():
            modificar(filme_achado)
            with open(caminho_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        else:
            novo_filme = str(input("O nome do filme não preenchido ou encontrado, digite um nome e tente novamente, ou escreva 'Sair' para sair.\n"))
            if novo_filme.lower() == "sair":
                os.system("clear")
            else:
                modificar_filmes(novo_filme)

