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

#Guardar dado
def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado_guardar = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado_guardar)
    dados_rolados.pop(dado_para_guardar)
    lista_final = [dados_rolados, dados_no_estoque]
    return lista_final

#Remover dado
def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado_remover = dados_no_estoque[dado_para_remover]
    dados_rolados.append(dado_remover)
    dados_no_estoque.pop(dado_para_remover)
    return[dados_rolados, dados_no_estoque]

#Calcula pontos na regra simples
def calcula_pontos_regra_simples(faces_rolados):
    pontos = {}
    i=1
    while i<=6:
        contador = faces_rolados.count(i)
        valor = contador*i
        pontos[i] = valor
        i+=1
    return pontos

#Calcula pontos na regra avançada - Soma
def calcula_pontos_soma(lista):
    soma = 0
    for nums in lista:
        soma += nums
    return soma

#Calcula pontos na regra avançada - Sequência baixa
def calcula_pontos_sequencia_baixa(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
        return 15
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 15
    if 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 15
    else:
        return 0
    
#Calcula pontos na regra avançada - Sequência alta
def calcula_pontos_sequencia_alta(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 30
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 30
    else:
        return 0
    
#Calcula pontos na regra avançada - Full House
def calcula_pontos_full_house(lista):
    for n in lista:
        if lista.count(n) == 3:
            for n2 in lista:
                if lista.count(n2) == 2:
                    return n*3 + n2*2
    return 0
