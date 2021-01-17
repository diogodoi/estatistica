import streamlit as st
import seaborn as sn
import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split

st.markdown("""
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
            * Números inteiros num intervalo chamamo de **Discretas**
            
        2. Qualitativos(Categóricos):

            * Categorias sem hieraquia chamamos de **Nominais**
            * Categorias **COM** hierarquia chamamos de **Ordinais** (ORDEM)
            """)

st.markdown("""       
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
""")

        
st.markdown(""" 
        ## Tipos de amostras
        
        ### Para o inicio do estudo vamos carregar o dataset Cannabis Strains.
        Esse dataset foi adquiro através do site [leafly.com](https://www.leafly.com/), e nos trás o nome da Planta, tipo, rating,efeitos,sabor e uma descrição feita por um usuário.
        ```python
        import pandas as pd
        data = pd.read_csv('cannabis.csv')
        data
        ```
        """)
data = pd.read_csv('cannabis.csv')
data

st.markdown("""Então a primeira coisa que precisamos investigar é a dimensão do dataset. Utilizando o seguite comando.
        
        data.shape
        """)
st.markdown("""         
         A saída é uma tupla, onde o primeiro valor é a quantidade de linhas e o segundo valor é a quantidade de colunas do seu dataset.
         """) 

data.shape 
        
st.markdown("""         
        * Aleatória Simples: É retirado um número determinado aleatóriamente da população.
            1. Com reposição
            2. Sem Reposição
            
        obs:Os elementos envolvidos devem ter a mesma chance de ser retiradas da população.
        Por exemplo
        
        ```python
        np.random.seed()
        
        # Dos 2351 valores 70% receberam o valor 0 e 30% o valor 1, onde sofreram reposição.        
        amostra = np.random.choice(a=[0,1], size = 2351, replace= True, p=[0.7,0.3])
        
        #Em seguida os valores =0 e =1 foram passados para o dataset, onde foram separados em dois datasets.
        valor0 = data.loc[amostra==0]
        valor1 = data.loc[amostra==1]

        valor0.shape
        valor1.shape
        ```
        """)
np.random.seed()
amostra = np.random.choice(a=[0,1], size = 2351, replace= True, p=[0.7,0.3])
valor0 = data.loc[amostra==0]
valor1 = data.loc[amostra==1]

valor0.shape
valor1.shape

st.markdown("""       
        * Estratificada: Quando a população está dividida em grupos. Então queremos que cada grupo tenha um elemento representativo.
        ```python
        from sklearn.model_selection import train_test_split
        # Agora vamos contar quantas plantas de cannabis pertencem a cada tipo utilizando a função .value_counts.
        data['Type'].value_counts()
        ```
        """)

tipos = data['Type'].value_counts()
tipos

st.markdown(""" A amostra estratificada procura manter a proporção dos dados. 
         
         Então utilizando o seguinte código:
         
         # A função train_test_split retorna 4 valores, no entanto oque nos interessa é somente o 3 valor, que aqui chamei de Y.
         # O primeiro parâmetro são as colunas que represetam os dados que nos iteressam, o segundo é a coluna que representa o tipo, o test_size 
         é decidida a proporção e o ultimo parâmetro stratify é decidada a coluna que sera usada como referencia para a estratificação.
         aqui os dados foram reduzidos proporcionalmente em 40%.
         X, _, Y, _ = train_test_split(data.iloc[:,[3,4,5]],data.iloc[:,1] ,test_size=0.6, stratify= data.iloc[:,1])
         
         # A seguir utilizamos a função value_counts() para verificar o novo dataset.
         Y.value_counts()
         """)


X, _, Y, _ = train_test_split(data.iloc[:,[3,4,5]],data.iloc[:,1] ,test_size=0.6, stratify= data.iloc[:,1])
Estrati = Y.value_counts()
Estrati

st.markdown(""" 
        * Sistemática: O primeiro elemento é escolhido de forma aleatória, a partir disso o próximo elemento é escolhi por uma regra. 
        obs: Utilizado quando não se tem a dimensão da população.
        ```python
        from math import ceil
        import random
        pop = 2351
        # Aqui delimitamos o valor da amostra desejada.
        amostra = 100
        c = ceil(pop/amostra)
        c
      
        ```
        """)
from math import ceil
import random
pop = 2351

amostra = 100
c = ceil(pop/amostra)
valor =  "A partir do primeiro valor aleatório a regra irá pegar a cada: " + str(c) + " valores."
valor
st.markdown("""
        Em seguida é necessário selecionar o primeiro valor para começar a contagem.    
        ```python
        r = np.random.randint(low = 1, high= k+1,size=1)
        ```
        """)
r = np.random.randint(low = 1, high= c+1,size=1)
valor_random = r[0]
resposta = "O valor aleatório gerado foi: " + str(valor_random) + "."
resposta
st.markdown("""
        ```python
        # Aqui foi selecionado o valor gerado aleatóriamente.
        val_selecionado = r[0]
        # Cria-se uma lista para que os valores gerados fiquem guardados.
        valores_sorteados = []
        # Então é criado um loop para que cada valor aleatório seja adicionado a lista.
        for i in range(amostra):
        sorteados.append(val_selecionado)
        val_selecionado+=c
        #Como eu sei o tamanho dos dados coloquei um limitador pra caso o valor ultrapasse o limite.
        if val_selecionado > 2351:
            break 
        valor_final = data.loc[valores_sorteados]
        valor_final
        ``` 
        """)
val_selecionado = r[0]
valores_sorteados = []
for i in range(amostra):
    valores_sorteados.append(val_selecionado)
    val_selecionado+=c
    if val_selecionado > 2351:
        break 
valor_final = data.loc[valores_sorteados]
valor_comprimento = "A nova amostra tem o tamanho de: " + str(len(valor_final)) + " valores."
valor_comprimento
valor_final

st.markdown("""         
        ## Medidas de Centralidade e Variabilidade
        
        Para esse estudo vamos levar em consideração a coluna ranting do nosso dataset.
        ```python
        data['Rating']
        
        ```
        """)
data['Rating']
st.markdown("""         
        * **Centralidade**
        """)

st.markdown("""         
1. Média: É o valor da soma de todos os elementos dividido pelo número total de elementos.
```python
#Vamos encontra qual foi a classificação média dada em cada planta através da função mean()        
data['Rating'].mean()         
```
         """)
media = data['Rating'].mean() 
media 
st.markdown("""        
2. Moda: É o valor mais comum entre os elementos.
```python
# E qual é o valor que mais aparece entre as classificações? Para isso utilizamos o comando mode()
data['Rating'].mode()

```
         """)
moda = data['Rating'].mode()
moda
st.markdown(""" 
3. Mediana: É o valor encontrado no centro dos dados.
```python
#Para encontrar o valor da mediana dos dados utilizamos o comando median()
data['Rating'].median()
```
         """)
mediana = data['Rating'].median()
mediana
st.markdown(""" 
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
        ```python
        # Para o estudo de variabilidade temos uma função salvadora da pátria a describe()
        data['Rating'].describe()
        ```
        
            """)

descricao = pd.DataFrame(data['Rating'].describe())
descricao1= ['Total de valores','Média','Desvio padrão','Valor minímo','Q1','Q2 ou Mediana','Q3','Valor Máximo']
descricao['Descrição'] = descricao1
descricao

st.markdown("""             
        ## Probabilidade
        
        Probabilidade(P) é o estudo para descobrir a "chance" de um evento acontecer.
        
        **Então os valores de P devem estar entre 0 e 1.**
        
        ### Como é calculado a probabilidade de um evento?
        """)
st.latex(r"""   
        P = \frac{Ocorrência Esperada}{Número de Eventos Possíveis}
""")
st.markdown("""        
        Ex: Qual a probabilidade de tirar 6 em um dado?
        """ )
st.latex(r"""        
        P = \frac{1}{6}        
""")
st.markdown("""         
        ### Conceitos
        
        * Experimento: É oque você que estudar Ex: Jogar uma moeda
        
        * Espaço amostral: É o conjunto de todas as possibilidade de ocorrer um evento. Ex: Cara ou Coroa
        
        * Evento: é o resultado do que ocorreu. Ex: Coroa

        Tipos de Eventos
        
        * Eventos excludentes: Quando o dois resultados não podem ocorrer ao mesmo tempo. Ex: jogar um dado e o resultado ser 1 e par.
        
        * Não excludentes: Quando podem ocorrer dois resultados ao mesmo tempo.Ex: jogar um dado e ser 2 e par.
        
        * Eventos dependentes: Um evento é afetado pelo outro. Um tem que acontecer para que o outro aconteça.
        
        * Eventos Indenpedentes: A ocorrência de um evento não afeta o outro evento.
        """)

st.markdown("""
                            
        ## Distribuição
        
        A Distribuição é usada na Teorida da Probabilidade, ela estuda o comportamento dos dados aleatórios.
        
        ### Distribuição Normal ou Gaussiana
        
        É uma distribuição onde os dados apresentam uma simetria, em formato de sino.
        É uma distribuição contínua.
        
        Como eu sei se uma amostra é uma distribuição Normal?
        
        1. Gerar um histograma.
        

""")
st.markdown("""  
```python
from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt
# Aqui é geramos dados com distribuição normal.
dados = norm.rvs(size=1000)
plt.hist(dados,bins = 20)
plt.title('Dados')
```
""")
from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt
dados = norm.rvs(size=1000)
fig, ax = plt.subplots()
ax.hist(dados,bins = 20)
plt.title('Dados')
st.pyplot(fig)
st.markdown("""  
        2. Diagrama de probabilidade Normal (qqplot)
        """)
st.markdown(""" 
            ```python
            fig, ax = plt.subplots()
            stats.probplot(dados,fit=True,plot=ax)
            plt.show
            ```
            """)
fig, ax = plt.subplots()
stats.probplot(dados,fit=True,plot=ax)
st.pyplot(fig)
st.markdown("""  
        3. Teste de Shapiro-Wilk onde: 
        
            * p-value <=0,05 Não normal
            
            * p-value > 0.05 Normal
            ```python
            #O teste de shapiro é bem simples, ele retorna uma tupla, onde o segundo valor revela o valor de p.
            stats.shapiro(dados)
            ```
            
            """)
shapiro = stats.shapiro(dados)
shapiro

st.markdown("""  
        * Distribuição Normal Padrão(Z): Serve de referência para a Distribuição normal. 
        >obs: Tem a média = 0 e desvio padrão = 1.
        
        Para transformar o valor da sua distribuição para o Z, usa-se a tabela Z.
        
        Assim utilizando a tabela Z é possível encontrar a probabilidade utilizando a seguinte fórmula:
        """)
st.latex(r'''    
            Z = \frac{X-u}{desvioPadrão}
''')           
st.markdown("""                 
        > X: é o valor que é proposto.
        
        > u: é a média.
        
        > std: é o desvio padrão.
        """)
st.markdown("""        
        ## Teorema Central do Limite
        
        Quanto maior a amostra, mais a distribuição se aproxima de uma distribuição normal.
                 
         """)


