# Instruções para uso adequado do código 

Na Classe Opers, temos 2 funções:  
- Na função deltait só existe um único parâmetro:
        data - onde se passa os dados como arrays
Seu retorno é um array n-dimensões normalizado por m-linhas.

- Na função mat_norm, 2 parâmetros é pedido:
        data - onde se passa os dados como arrays
        
        med - True ou False. Caso seja True, o resultado é uma matriz normalizada com auxílio da função deltait.  
Temos 2 retornos, o primeiro que vamos denominar aqui por a e o segundo por b. O retorno a é normalizado e é utilizado para plotarmos um "mapa de calor", e o retorno b faz uso do produto escalar e serve para o "histograma de Parisi".         
