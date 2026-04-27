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