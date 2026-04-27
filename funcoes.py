#Rolar Dados
import random

def rolar_dados(n):
    dados_rolados = []
    i = 1
    while i <= n:
        dado = random.randint(1,6)
        dados_rolados.append(dado)
        i+=1
    return dados_rolados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado_guardar = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado_guardar)
    dados_rolados.pop(dado_para_guardar)
    lista_final = [dados_rolados, dados_no_estoque]
    return lista_final