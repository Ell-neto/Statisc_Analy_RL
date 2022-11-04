# Instructions to use the code 💻

The plots below are from three different datasets, named data1 the [Dados_Iz](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/data/Dados_Iz.xlsx), data2 (for input power [2.45Pth](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/data/PPth245.xlsx)) and data3 (for input power [3.6mJ](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/data/3.6mJ.xlsx)).  

In the **Class Opers**, we have two functions:  
- In function deltait, there is only a single parameter:  

        data - Please inform data as arrays  
The return is an n-dimensional array normalized by m-lines.

- In function mat_norm, two parameters must be entered:

        data - Please inform data as arrays
        
        med - None (default). If True, the outcome is a matriz normalized using the function deltait.
We obtain two returns, the first named "a" and the second named "b". Outcome "a" is normalized and is used to plot a heatmap, whereas return "b" gives Parisi histogram.           


Na **Classe GrafsIzra**, temos apenas uma função (fit_izra), pois é dedicado exclusivamente ao modelo Izrailev, com seus parâmetros:  

        data - Please inform data as arrays
        
        model - Algumas funções determinadas do modelo Izrailev, sendo as opções 'izrailev4', 'izrailev6', 'izrailev8' e izrailev10'
        
        density - True ou False
        
        color1 - Cor do histograma, usamos as cores disponíveis do matplotlib em https://matplotlib.org/stable/gallery/color/named_colors.html
        
        color2 - Cor da função, usamos as cores disponíveis do matplotlib em https://matplotlib.org/stable/gallery/color/named_colors.html
        
        title - Título do gráfico
        
        glog - None (default). Caso seja True, cria um scatter do histograma + função com eixos na escala log x log.
        
A função tem dois retornos, os parâmetros das variáveis do modelo Izrailev escolhido e uma matriz covariância (erro). Como podemos conferir abaixo os retornos para o modelo de 'Izrailev4', e utilizamos o data1:
![par_error](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/fig_param_erro.png)  
E ainda plota um histograma com uma função do modelo de Izrailev escolhido caso o glog seja None (📊+📈).
![grafa1](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_1a.png)
![grafb1](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_2a.png)  
E caso glog seja True, o modelo Izrailev é plotado na escala logxlog com scatter, como vemos abaixo.
![grafa2](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_1b.png)
![grafb2](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_2b.png)  
OBS: Os gráficos da escala log são da mesma seleção de dados sem a escala log.  

Na **Classe GrafsVar** temos quatro funções, vamos descrever cada uma;
- A função sohist, que é um histograma comum 📊, com os parâmetros:  

        data - Please inform data as arrays
        
        density - True ou False
        
        color - Cor do histograma, usamos as cores disponíveis do matplotlib em https://matplotlib.org/stable/gallery/color/named_colors.html
        
        title - Título do gráfico  
Para o data3, e fazendo uso do segundo retorno da função mat_norm, plotamos o histograma de Parisi.
![hist_parisi](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/36_histoparisi.png)

- A função varii, que nos dá uma noção da faixa de intensidade máxima nos dados 📈, com os parâmetros:

        data - Please inform data as arrays
        
        vall - Caso deseje ter uma faixa inicial para plotar o gráfico (muito útil para dados muito grandes)
        
        title - Título do gráfico  
 Para o data2, obtemos o gráfico abaixo.  
 ![varii](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/intens_max.png)  
 
 - A função grafs_a plota um gráfico 3D, uma observação importante é que tem um retorno (colocado para saber qual faixa de intensidade está sendo utilizada no momento que gerou o gráfico), e esse retorno é um valor aleatório escolhido para as intensidades (por isso o uso do randint), e seus parâmetros são:
        
        data - Please inform data as arrays
        
        title - Título do gráfico  

        titlex - Nome do eixo x

        titley - Nome do eixo y
     
        titlez - Nome do eixo z 
        
Para o data3, obtemos o gráfico  
![graf36](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/3d_36.png)
E ainda para outro conjunto de dados, podemos obter.  

![gra56](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/fig56.png)  
OBS: Lembrando que o espectro é configurado como 1000.

- A função ht_map é um "mapa de calor", fazemos uso dele para os coeficientes das correlações de Pearson. Seus parâmetros são:

        a - Please inform data
        
        cmap - Escolha o colormap, disponível em https://matplotlib.org/stable/tutorials/colors/colormaps.html
        
        title - Título do gráfico  

        titlex - Nome do eixo x

        titley - Nome do eixo y
     
Para o data3, e lembrando que fazemos uso do primeiro retorno da função mat_norm, obtemos o seguinte mapa.  
![graf36map](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/36_mapcalor.png)  

E ainda para outro conjunto de dados, obtemos.  
![map47](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/mp_cal47.png)  


*Observação final: Todos os gráficos estão ajustados para tratar com um determinado conjunto de dados, caso seus dados tenham muitas casas decimais ou sejam um conjunto enorme (tipo, enorme mesmo (risos)), deverá ajustar os dados de main.py para de acordo com o que se deseja, levando em conta que todos os gráficos já são previamente definidos, ou seja, já tem determinados valores nos eixos, determinados valores nos conjuntos dados, e pode sim mexer com o main.py para atribuir outros casos e outros valores, isso que é divertido em computação! E para quaisquer dúvidas e/ou esclarecimento, por favor, pode entrar em contato com o [autor✉️](mailto:manoelfsneto@live.com).*
