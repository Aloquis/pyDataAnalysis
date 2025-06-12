import numpy as np
import pandas as pd
import matplotlib.pylab as plot

from leitorCSV import carregar_csv_para_dicionario

nomes = ['Temperatura', 'Energia(Gcal/h)', 'Alimentação(T/h)']
dados_extraidos = carregar_csv_para_dicionario("dadosFinais.csv", nomes)

X = list(dados_extraidos.values())
temp_atual = dados_extraidos["Temperatura"]
X = np.array(X).T

#lambda é o chamado fator de esquecimento.

def rls(temp_atual, historico_regressores, lam=0.96, n=1000, num_passos=100):

    vetor_parametros = np.zeros((3, 1)) # vetor coluna

    matriz_covariancia = n * np.eye(3) #Calculo da primeira matriz de covariância

    temp_pred = [] #Lista que contem as temperaturas preditas

    for k in range((num_passos - 1)):
        
        regressores_em_k = historico_regressores[k].reshape(-1, 1) # reshape -> coluna

        ganho_t = matriz_covariancia @ regressores_em_k / (lam + regressores_em_k.T @ matriz_covariancia @ regressores_em_k)

        erro = temp_atual[k+1] - (regressores_em_k.T @ vetor_parametros)

        vetor_parametros = vetor_parametros + ganho_t * erro 
        
        matriz_covariancia = (matriz_covariancia - ganho_t @ regressores_em_k.T @ matriz_covariancia) / lam
        temp_pred.append(float((regressores_em_k.T @ vetor_parametros).item()))
        
        print(f'A: {vetor_parametros[0].item():.3f}')
        print(f'B: {vetor_parametros[1].item():.3f}')
        print(f'C: {vetor_parametros[2].item():.3f}')

    COEF_A = float(vetor_parametros[0].item())
    COEF_B = float(vetor_parametros[1].item())
    COEF_C = float(vetor_parametros[2].item())


    return np.array(temp_pred), COEF_A, COEF_B, COEF_C

temp_pred, COEF_A, COEF_B, COEF_C = rls(temp_atual, X)
print(f"A: {COEF_A:.3f}, B: {COEF_B:.3f}, C: {COEF_C:.3f}")

plot.figure(1)
plot.plot(temp_pred)
plot.title('Temperatura predita')
plot.xlabel('Passo (k+1)')
plot.ylabel('')
plot.grid(True)


plot.figure(2)
plot.plot(temp_atual)
plot.title('Temperatura real')
plot.xlabel('Passo (k)')
plot.ylabel('')
plot.grid(True)
plot.show()
