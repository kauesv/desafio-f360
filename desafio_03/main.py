'''
Escreva uma função que receba uma lista de inteiros (representando valores de
transações diárias) e retorne a maior soma de um subarray contínuo (subconjunto de
transações).
'''

def maior_soma_subarray(lista):
    """Encontra a maior soma em um subarray"""
    # Verifica se a lista está vazia
    if not lista:
        return [], 0

    # armazena a soma máxima do subarray contíguo encontrado até o momento
    maximo_ate_agora = lista[0]
    # armazena a soma máxima do subarray contíguo termina no índice atual
    max_terminando_aqui = lista[0]

    indice_inicial = 0
    indice_final = 0
    temp_inicial = 0

    for i in range(1, len(lista)):
        print(i)
        print(f"max_terminando_aqui: {max_terminando_aqui}")

        # Se a soma corrente for negativa, reinicia a soma e atualiza o índice inicial
        if max_terminando_aqui < 0:
            max_terminando_aqui = lista[i]
            temp_inicial = i
        else:
            max_terminando_aqui += lista[i]

        print(f"max_terminando_aqui: {max_terminando_aqui}")

        # Atualiza o máximo encontrado até agora
        if max_terminando_aqui > maximo_ate_agora:
            maximo_ate_agora = max_terminando_aqui

            #Atualiza os indices 
            indice_inicial = temp_inicial
            indice_final = i

        print(f"maximo_ate_agora: {maximo_ate_agora}")

        # se as somas ainda forem menor que zero, atualize para zero novamente,
        # para que o loop descarte os negativos
        # if max_terminando_aqui < 0:
        #     print('Zerou')
        #     max_terminando_aqui = 0

    print('index_inicial', indice_inicial)
    print('index_final', indice_final)
    print(lista[indice_inicial:indice_final+1])
    return lista[indice_inicial:indice_final+1], maximo_ate_agora