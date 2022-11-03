# Instruções para uso adequado do código 

Na **Classe Opers**, temos 2 funções:  
- Na função deltait só existe um único parâmetro:

        data - onde se passa os dados como arrays  
Seu retorno é um array n-dimensões normalizado por m-linhas.

- Na função mat_norm, 2 parâmetros é pedido:

        data - onde se passa os dados como arrays
        
        med - None (default). Caso seja True, o resultado é uma matriz normalizada com auxílio da função deltait.  
Temos dois retornos, o primeiro que vamos denominar aqui por a e o segundo por b. O retorno a é normalizado e é utilizado para plotarmos um "mapa de calor", e o retorno b faz uso do produto escalar e serve para o "histograma de Parisi".           


Na **Classe GrafsIzra**, temos apenas uma função, pois é dedicado exclusivamente ao modelo Izrailev, com seus parâmetros:  

        data - onde se passa os dados como arrays
        
        model - Algumas funções determinadas do modelo Izrailev, sendo as opções 'izrailev4', 'izrailev6', 'izrailev8' e izrailev10'
        
        density - True ou False
        
        color1 - Cor do histograma, usamos as cores disponíveis do matplotlib em https://matplotlib.org/stable/gallery/color/named_colors.html
        
        color2 - Cor da função, usamos as cores disponíveis do matplotlib em https://matplotlib.org/stable/gallery/color/named_colors.html
        
        title - Título do gráfico
        
        glog - None (default). Caso seja True, cria um scatter do histograma + função com eixos na escala log x log.
        
A função tem dois retornos, os parâmetros das variáveis do modelo Izrailev escolhido e uma matriz covariância (erro). Como podemos conferir abaixo os retornos para o modelo de 'Izrailev4':
![par_error](/img/fig_param_erro.png)  
E ainda plota um histograma com uma função do modelo de Izrailev escolhido caso o glog seja None.
![grafa1](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_1a.png)
![grafb1](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_2a.png)  
E caso glog seja True, o modelo Izrailev é plotado na escala logxlog com scatter, como vemos abaixo.
![grafa2](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_1b.png)
![grafb2](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_2b.png)  
OBS: Os gráficos da escala log são da mesma seleção de dados sem a escala log.
