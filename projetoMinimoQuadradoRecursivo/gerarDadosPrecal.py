import pandas as pd
import numpy as np
import matplotlib.pyplot as plot


plot.close('all')

# DEFINA O NÚMERO DE PASSOS
num_passos = 100


# COEFICIENTES
COEF_A = 0.9
COEF_B = 2.75
COEF_C = -1.70


# CONDIÇÕES INICIAIS
ENERGIA_INICIAL = 100
TEMPERATURA_INICIAL = 850
ALIMENTACAO_INICIAL = 100

# PARÂMETROS PARA GERAR OS DADOS
    #ENERGIA
VARIACAO_ENERGIA_DECRESCIMENTO = 1 
VARIACAO_ENERGIA_CRESCIMENTO = 0.5
LIMITE_PASSOS_DECRESCIMO_ENERGIA = 20
    #ALIMENTACAO
VARIACAO_ALIMENTACAO_CRESCIMENTO = 0.5
LIMITE_MAX_ALIMENTACAO = 150


def gerarDadosEnergia(num_passos, inicial, limite_passos_decrescimo, 
                      variacao_decresimo, variacao_acrescimo):

    historico = []
    valor_atual = float(inicial)

    for k in range(num_passos):
        if k < limite_passos_decrescimo:
            valor_atual -= np.random.uniform(0, variacao_decresimo)
        else:
            valor_atual += np.random.uniform(0, variacao_acrescimo)
        historico.append(valor_atual)

    return historico

def gerarDadosAlimentacao(num_passos, inicial, limite_k, variacao_acrescimo):

    historico = []
    valor_atual = inicial

    for k in range (num_passos):
        if valor_atual < limite_k:
            valor_atual += np.random.uniform(0, variacao_acrescimo)
        historico.append(valor_atual)

    return historico

def gerarDadosTemperatura(num_passos, historico_energia, historico_alimentacao, COEF_A, COEF_B, COEF_C):

    historico = []

    for k in range (num_passos):

        if k == 0:
            #Operação
            temperatura_em_k = (COEF_A * TEMPERATURA_INICIAL) + \
            (COEF_B * ENERGIA_INICIAL) + \
            (COEF_C * ALIMENTACAO_INICIAL)

            #Updates
            historico.append(temperatura_em_k)
            #delta_c.append(0)

        else:
            #Operação
            temperatura_em_k = ((COEF_A * historico[k - 1]) + \
                                (COEF_B * historico_energia[k-1]) + \
                                (COEF_C * historico_alimentacao[k-1]))
            #Updates
            historico.append(temperatura_em_k)

    return historico

energia_historico = gerarDadosEnergia(num_passos, ENERGIA_INICIAL, LIMITE_PASSOS_DECRESCIMO_ENERGIA, 
                                      VARIACAO_ENERGIA_DECRESCIMENTO, VARIACAO_ENERGIA_CRESCIMENTO)

alimentacao_historico = gerarDadosAlimentacao(num_passos, ALIMENTACAO_INICIAL, LIMITE_MAX_ALIMENTACAO, 
                                              VARIACAO_ALIMENTACAO_CRESCIMENTO)

temperatura_historico = gerarDadosTemperatura(num_passos, energia_historico, alimentacao_historico, COEF_A, COEF_B, COEF_C)


mapaDosValores = {
    'Temperatura' : temperatura_historico,
    'Energia(Gcal/h)' : energia_historico,
    #'Controle Aplicado' : delta_c,
    'Alimentação(T/h)' : alimentacao_historico
}

DataHistoricos = pd.DataFrame(mapaDosValores)

print(DataHistoricos.describe())

DataHistoricos.to_csv('dadosFinais.csv', index = False)

plot.figure(1)
plot.plot(alimentacao_historico)
plot.title('Evolução da alimentação')
plot.xlabel('Passo (k)')
plot.ylabel('Alimentação (T/h)')
plot.grid(True)

plot.figure(2)
plot.plot(temperatura_historico)
plot.title('Evolução da temperatura')
plot.xlabel('Passo (k)')
plot.ylabel('Temperatura (°C)')
plot.grid(True)

plot.figure(3)
plot.plot(alimentacao_historico, temperatura_historico)
plot.title('Temp em função da Alimentação')
plot.xlabel('Alimentação (T/h)')
plot.ylabel('Temperatura (°C)')
plot.grid(True)
plot.show()