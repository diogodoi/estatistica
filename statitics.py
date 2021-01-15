import streamlit as st
import seaborn as sn
import pandas as pd
import numpy as np


st.write("""
        # Estatítisca I
         
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
         
         
         """)