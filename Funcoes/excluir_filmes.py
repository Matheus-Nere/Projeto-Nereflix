import json
import os
import time

pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_script, "..", "Catalogo", "lista_filmes.json")
caminho_json = os.path.abspath(caminho_json)

def achar (dados, filme):
    
    for i in dados:
        if i['nome'].lower() == filme.lower():
           
            filme_achado = i
            return filme_achado

def excluir_filme (filme):
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
                dados_existentes = json.load(arquivo)
                filme_achado = achar(dados_existentes, filme)
    if filme_achado:
        print("filme excluido com sucesso. ")
        print()
        time.sleep(2)
        if filme and filme_achado["nome"].lower() == filme.lower():
            dados_existentes.remove(filme_achado)
            with open(caminho_json, "w", encoding="utf-8") as arquivo_escrita:
                json.dump(dados_existentes, arquivo_escrita, ensure_ascii=False, indent=4)
    else:
            os.system("clear")
            sai = input("Filme não encontrado. Se quiser buscar novamente digite 'Sim', caso deixe em branco e aperte 'Enter'': ")
            print()
            if sai.lower() == "sim":
                filme = str(input("Digite o nome do filme quer deseja excluir: \n"))
                excluir_filme(filme)



