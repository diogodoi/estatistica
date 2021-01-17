import streamlit as st
import seaborn as sn
import pandas as pd
import numpy as np
import random
st.write("""
        # Estatítisca 
         
        ## A estatística pode ser dividida em 3 áreas:   
             
        ### 1. Descritiva
        
        A estatisitca Descritiva, busca explorar e resumir os dados através de gráficos e tabelas. 
        Ela traz uma compreensão dos dados em que vocês está trabalhando. Análise Exploratória dos Dados (AED).
        
        ### 2. Probabilistica
        
        A estatistica Probabilisca, busca analisar situações que estão sujeitas ao acaso. Ex: jogar uma moeda, encontrar uma agulha no palheiro.  
        
        ### 3. Inferencial
        
        A estatistica Inferencial bucas obter respostas de um fenônemno com dados representativos. Ou seja ela busca uma resposta para uma pergunta através de uma *AMOSTRA*.
         
        ## Observação X Experimento
        
        A Observação é um estudo onde os elementos análisados não são afetados.Ex: Estudo da peferência de voto em um certo candidato.
        No Experimento são impostos condições ou tratamentos a grupos, para que assim o resultado possa ser avaliado. Ex: Estudo de uma vacina em uma PANDEMIA.
        
        ## Tipos de Dados
        
        ### Os dados podem ser separados em duas categorias:
        1. Quantitativos(Númericos):

            * Valores reais que podem assumir qualquer intervalo chamamos de **Contínuas**
            * Números inteiros num intervalo **Discretas**
            
        2. Qualitativos(Categóricos):

            * Categorias sem hieraquia chamamos de **Nominais**
            * Categorias **COM** hierarquia chamamos de **Ordinais** (ORDEM)
            
         
         ## Amostra       
         
         Uma amostra é uma parte de uma população. Uma amostra feita corretamente, representa as características da população na qual foi retirada.
                  
         Se essa amostra não represetar a população, dizemos que ela é enviesada.
         
         ### Oque pode causar um enviesamento?
         
        * Quando você **SUB**estima ou **SUPER**estima algum parâmetro da população.
        
        * Por isso sempre que se for tirar uma amostra é necessário utilziar de mecanismos de seleção aleatória.
        
        Existem custos ao se trabalhar com uma amostra.Por isso ao se falar de amostra procuramos entender sua:
        
        1. **Margem de Erro e Nível de Confiança**
        2. Variação, pois diferentes amostras podem gerar resultados diferentes.
        3. Além disso é possivel "medir" essa variação esperada.
         
        ## Tipos de amostras
        
        * Aleatória Simples:É retirado um número determinado aleatóriamente da população.
            1. Com reposição
            2. Sem Reposição
            
        obs:Os elementos envolvidos devem ter a mesma chance de ser retiradas da população.
        
        * Estratificada: Quando a população está dividida em grupos. Então queremos que cada grupo tenha um elemento representativo.
        
        * Sistemática:O primeiro elemento é escolhido de forma aleatória, a partir disso o próximo elemento é escolhi por uma regra. 
        obs: Utilizado quando não se tem a dimensão da população.
        
        ## Medidas de Centralidade e Variabilidade
        
        * **Centralidade**
        
         1. Média: É o valor da soma de todos os elementos dividido pelo número total de elementos.
         2. Moda: É o valor mais comum entre os elementos.
         3. Mediana: É o valor encontrado no centro dos dados.
         
         * **Variabilidade**
         
         1. Variância: Mostra a regularidade dos dados, como os dados variam diante da média.
         2. Desvio padrão: Quanto maior, mais afastados da média.
         3. Amplitude: Diferença entre o maior e o menor valor
         4. Não Centrais: Quartis
            * Q0 mostra o menor valor
            * Q1 mostra 25% dos menores valores 
            * Q2 50% dos valores(MEDIANA) 
            * Q3 75% dos maiores valores
            * Q4 mostra o maior valor
            
        ## Probabilidade
        
        Probabilidade é o estudo para descobrir a "chance" de um evento acontecer.
        
        Probabilidade(P): 0 <- P <- 1
        
        Ex: Descobrir a chance de se tirar cara ou coroa ao lançar uma moeda.
        
        ### Como é calculado a probabilidade de um evento?
        
        P = Ocorrência Esperada/Número de Eventos Possíveis
        
        Ex: Qual a probabilidade de tirar 6 em um dado?
        
        P = 1/6        
        
        ### Conceitos
        
        * Experimento: É oque você que estudar Ex: Jogar uma moeda
        
        * Espaço amostral: É o conjunto de todas as possibilidade de ocorrer um evento. Ex: Cara ou Coroa
        
        * Evento: é o resultado do que ocorreu. Ex: Coroa

        Tipos de Eventos
        
        * Eventos excludentes: Quando o dois resultados não podem ocorrer ao mesmo tempo. Ex: jogar um dado e o resultado ser 1 e par.
        
        * Não excludentes: Quando podem ocorrer dois resultados ao mesmo tempo.Ex: jogar um dado e ser 2 e par.
        
        * Eventos dependentes: Um evento é afetado pelo outro. Um tem que acontecer para que o outro aconteça.
        
        * Eventos Indenpedentes: A ocorrência de um evento não afeta o outro evento.
                
        ## Distribuição
        
        A Distribuição é usada na Teorida da Probabilidade, ela estuda o comportamento dos dados aleatórios.
        
        ### Distribuição Normal ou Gaussiana
        
        É uma distribuição onde os dados apresentam uma simetria, em formato de sino.
        É uma distribuição contínua.
        
        Como eu sei se uma amostra é uma distribuição Normal?
        
        1. Gerar um histograma.
        2. Diagrama de probabilidade Normal (qqplot)
        3. Teste de Shapiro-Wilk onde: 
        
            * p-value <=0,05 Não normal
            
            * p-value > 0.05 Normal

        * Distribuição Normal Padrão(Z): Serve de referência para a Distribuição normal. 
        obs:Tem a média = 0 e desvio padrão = 1.
        
        Para transformar o valor da sua distribuição para o Z, usa-se a tabela Z.
        
        Assim utilizando a tabela Z é possível encontrar a probabilidade utilizando a seguinte fórmula:
            
            Z = X - u / std
                
        * X: é o valor que é proposto.
        * u: é a média.
        * std: é o desvio padrão.
        
        ## Teorema Central do Limite
        
        Quanto maior a amostra, mais a distribuição da média se aproxima de uma distribuição normal.
        
        ### Agora que entendemos um pouco do conceito, vamos aplicar no dataset abaixo.
        
         
         """)

data = pd.read_csv('cannabis.csv')
data
