import pandas as pd
import numpy as np
import Models.main as mi

# dados = pd.read_excel(r"C:\Users\Manoel\Downloads\Dados_Iz.xlsx", engine="openpyxl")
# dados = pd.read_excel(r"C:\Users\Manoel\Downloads\PPth245.xlsx", engine="openpyxl")
dados = pd.read_excel(r"C:\Users\Manoel\Downloads\3.6mJ.xlsx", engine="openpyxl")

dados_np = np.array(dados)


################# Exemplos com Dados_Iz #########################

# Plotar apenas os histogramas
# mi.GrafsVar.sohist(dados_np[:,0],True,'teal')

# Plotar gráficos com histograma e modelo junto
# pars, erro = mi.GrafsIzra.fit_izra(dados_np[:,5], 'izrailev4', True, 'teal', 'purple')
# print(f"Os valores dos parâmetros são: {pars}")
# print(f"A matriz de covariância é:\n {erro}")

# Plotar gráficos na escala log-log
# pars, erro = mi.GrafsIzra.fit_izra(dados_np[:,14], 'izrailev4', True, 'white', 'purple', glog=True)
# print(f"Os valores dos parâmetros são: {pars}")
# print(f"A matriz de covariância é:\n {erro}")

# Exemplo para criar series temporais
# No conjunto de dados, onde cada gráfico representa a 'quantidade de colunas', logo, 20 series.
# for i in range(dados_np.shape[1]):
#     pars, erro = mi.GrafsIzra.fit_izra(dados_np[:,i], 'izrailev4', True, 'teal', 'purple')
#     print(f"Os valores dos parâmetros da figura {i} são: {pars}")


############ Plotar com os demais dados, por exemplo, com PPth245 e 3.6mJ ####################

# Gráfico 3D de 1000 perfis de espectro
# dados_dec = (dados_np.T)/10**18
# a = mi.GrafsVar.grafs_a(dados_dec, 'Titulo do grafico', 'eixo x', 'eixo y', 'eixo z')
# print(a)

# Gráfico para visualizar a intensidade máxima
# mi.GrafsVar.varii(dados_np.T, 100)

# O mat_norm tem 2 saídas, a saída do exemplo abaixo zz trata os dados para plotarmos um mapa de calor, o ss trata os dados para o histograma de Parisi
# zz, ss = mi.Opers.mat_norm(dados_np.T, True)
# mi.GrafsVar.sohist(ss,True,'teal')

# Gráfico de mapa de calor do coeficiente de correlação de Pearson
# zzs = zz[450:650, 450:650]
# mi.GrafsVar.ht_map(zzs, 'jet')
