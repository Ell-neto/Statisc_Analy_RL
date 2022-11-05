import pandas as pd
import numpy as np
from matplotlib import cm
import Models.main as mi

# data = pd.read_excel(r"C:\Users\Manoel\Downloads\Dados_Iz.xlsx", engine="openpyxl")
# data = pd.read_excel(r"C:\Users\Manoel\Downloads\PPth245.xlsx", engine="openpyxl")
data = pd.read_excel(r"C:\Users\Manoel\Downloads\3.6mJ.xlsx", engine="openpyxl")

data_np = np.array(data)


################# Exemplos com Dados_Iz #########################

# Plot only the histogram
# mi.GrafsVar.sohist(data_np[:,0],True,'teal')

# Plot graphs with histogram and model together
# pars, error = mi.GrafsIzra.fit_izra(data_np[:,5], 'izrailev4', True, 'teal', 'purple')
# print(f"The parameter values are: {pars}")
# print(f"The covariance matrix:\n {error}")

# Plot graphs on log-log scale
# pars, error = mi.GrafsIzra.fit_izra(data_np[:,5], 'izrailev4', True, 'white', 'purple', "4", glog=True)
# print(f"The parameter values are: {pars}")
# print(f"A matriz de covariância é:\n {error}")

# Example for creating time series
# In our dataset, where each graph represents the 'number of columns', so 20 series.
# for i in range(dados_np.shape[1]):
#     pars, error = mi.GrafsIzra.fit_izra(data_np[:,i], 'izrailev4', True, 'teal', 'purple')
#     print(f"The values of the parameters in figure {i} are:: {pars}")


############ Plot with the other data, for example with Pth245 and 3.6mJ ####################

# 3D graphic of 1000 spectrum profiles
# data_dec = (data_np.T)/10**18
# a = mi.GrafsVar.grafs_a(data_dec, cm.jet,'Graph Title', 'X axis', 'Y axis', 'Z axis')
# print(a)

# Graph to view maximum intensity
# mi.GrafsVar.varii(data_np.T,'green', 100)

# The mat_norm has 2 returns, the return of the example below zz handles the data for us to plot a heat map, the ss handles the data for the Parisi histogram
# zz, ss = mi.Opers.mat_norm(data_np.T, True)
# mi.GrafsVar.sohist(ss,True,'teal')

# Pearson correlation coefficient heat map plot
# zzs = zz[450:650, 450:650]
# mi.GrafsVar.ht_map(zzs, 'jet')
