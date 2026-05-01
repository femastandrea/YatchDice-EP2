#Jogo
import random


def rolar_dados(n):
    dados_rolados = []
    i = 1
    while i <= n:
        dado = random.randint(1, 6)
        dados_rolados.append(dado)
        i += 1
    return dados_rolados


def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado_guardar = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado_guardar)
    dados_rolados.pop(dado_para_guardar)
    return [dados_rolados, dados_no_estoque]


def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado_remover = dados_no_estoque[dado_para_remover]
    dados_rolados.append(dado_remover)
    dados_no_estoque.pop(dado_para_remover)
    return [dados_rolados, dados_no_estoque]


def calcula_pontos_regra_simples(faces_rolados):
    pontos = {}
    i = 1
    while i <= 6:
        contador = faces_rolados.count(i)
        pontos[i] = contador * i
        i += 1
    return pontos


def calcula_pontos_soma(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma


def calcula_pontos_sequencia_baixa(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
        return 15
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 15
    if 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 15
    return 0


def calcula_pontos_sequencia_alta(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 30
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 30
    return 0


def calcula_pontos_full_house(lista):
    for n in lista:
        if lista.count(n) == 3:
            for n2 in lista:
                if lista.count(n2) == 2:
                    return n * 3 + n2 * 2
    return 0


def calcula_pontos_quadra(lista):
    soma = calcula_pontos_soma(lista)
    for num in lista:
        if lista.count(num) >= 4:
            return soma
    return 0


def calcula_pontos_quina(lista):
    for num in lista:
        if lista.count(num) >= 5:
            return 50
    return 0


def calcula_pontos_regra_avancada(lista):
    dic = {}
    dic['cinco_iguais'] = calcula_pontos_quina(lista)
    dic['full_house'] = calcula_pontos_full_house(lista)
    dic['quadra'] = calcula_pontos_quadra(lista)
    dic['sem_combinacao'] = calcula_pontos_soma(lista)
    dic['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
    dic['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista)
    return dic


def faz_jogada(lista, string, dic):
    if string in [1, 2, 3, 4, 5, 6] or string in ['1', '2', '3', '4', '5', '6']:
        categoria = int(string)
        x = calcula_pontos_regra_simples(lista)
        dic['regra_simples'][categoria] = x[categoria]
    else:
        x = calcula_pontos_regra_avancada(lista)
        dic['regra_avancada'][string] = x[string]
    return dic


def imprime_cartela(cartela):
    print("\n=== CARTELA ===")
    print("--- Regra Simples ---")
    for k, v in cartela['regra_simples'].items():
        valor = str(v) if v != -1 else "---"
        print(f"  {k}: {valor}")
    print("--- Regra Avançada ---")
    for k, v in cartela['regra_avancada'].items():
        valor = str(v) if v != -1 else "---"
        print(f"  {k}: {valor}")
    print("===============\n")


def eh_inteiro_nao_negativo(s):
    if len(s) == 0:
        return False
    for c in s:
        if c < "0" or c > "9":
            return False
    return True


def cartela_vazia():
    return {
        "regra_simples": {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
        "regra_avancada": {
            "sem_combinacao": -1,
            "quadra": -1,
            "full_house": -1,
            "sequencia_baixa": -1,
            "sequencia_alta": -1,
            "cinco_iguais": -1
        }
    }


def linha_ja_preenchida(cartela, combinacao):
    if eh_inteiro_nao_negativo(combinacao):
        n = int(combinacao)
        if n in cartela["regra_simples"]:
            return cartela["regra_simples"][n] != -1
        return False
    if combinacao in cartela["regra_avancada"]:
        return cartela["regra_avancada"][combinacao] != -1
    return False


def combinacao_existe(cartela, combinacao):
    if eh_inteiro_nao_negativo(combinacao):
        return int(combinacao) in cartela["regra_simples"]
    return combinacao in cartela["regra_avancada"]


def mostrar_dados(rolados, guardados):
    print(f"Dados rolados: {rolados}")
    print(f"Dados guardados: {guardados}")


def calcula_pontuacao_total(cartela):
    soma_simples = 0
    for v in cartela["regra_simples"].values():
        if v != -1:
            soma_simples += v
    soma_avancada = 0
    for v in cartela["regra_avancada"].values():
        if v != -1:
            soma_avancada += v
    bonus = 35 if soma_simples >= 63 else 0
    return soma_simples + soma_avancada + bonus


def jogo():
    cartela = cartela_vazia()
    imprime_cartela(cartela)

    for jogada in range(12):
        dados_rolados = rolar_dados(5)
        dados_guardados = []
        rerrolagens_usadas = 0
        jogada_feita = False
        mostrar_status = True

        while not jogada_feita:
            if mostrar_status:
                mostrar_dados(dados_rolados, dados_guardados)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            mostrar_status = True
            opcao = input()

            if opcao == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                g = input()
                if eh_inteiro_nao_negativo(g) and 0 <= int(g) < len(dados_rolados):
                    resultado = guardar_dado(dados_rolados, dados_guardados, int(g))
                    dados_rolados = resultado[0]
                    dados_guardados = resultado[1]

            elif opcao == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                g = input()
                if eh_inteiro_nao_negativo(g) and 0 <= int(g) < len(dados_guardados):
                    resultado = remover_dado(dados_rolados, dados_guardados, int(g))
                    dados_rolados = resultado[0]
                    dados_guardados = resultado[1]

            elif opcao == "3":
                if rerrolagens_usadas >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    n_para_rolar = 5 - len(dados_guardados)
                    dados_rolados = rolar_dados(n_para_rolar)
                    rerrolagens_usadas += 1

            elif opcao == "4":
                imprime_cartela(cartela)

            elif opcao == "0":
                todos_dados = dados_rolados + dados_guardados
                print("Digite a combinação desejada:")
                escolha_valida = False
                while not escolha_valida:
                    combinacao = input()
                    if not combinacao_existe(cartela, combinacao):
                        print("Combinação inválida. Tente novamente.")
                    elif linha_ja_preenchida(cartela, combinacao):
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(todos_dados, combinacao, cartela)
                        escolha_valida = True
                        jogada_feita = True

            else:
                print("Opção inválida. Tente novamente.")
                mostrar_status = False

    imprime_cartela(cartela)
    pontuacao = calcula_pontuacao_total(cartela)
    print(f"Pontuação total: {pontuacao}")


jogo()