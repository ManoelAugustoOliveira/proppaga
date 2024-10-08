# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:24:27 2024

@author: ManoelAugusto
"""
# In[]
!pip install pandas 
!pip install matplotlib
!pip install seaborn 
!pip install selenium

# In[]
import pandas as pd # Tratamento da base de dados
import matplotlib.pyplot as plt # Visualização dos dados
import seaborn as sns # Visualização dos dados

# Web scraping https://selenium-python.readthedocs.io/index.html
from selenium import webdriver
from selenium.webdriver.common.by import By

# In[]
################################# Leitura e extração dos dados ##########################################

# Leitura da base de dados das ações que compõem o índice ibovespa (adaptado).
# data de referencia 30/09/2024
# https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm

df = pd.read_csv('IBOVDia_30-09-24.csv')

# Total de ativos
df.shape

# Inicializa as variáveis que serão extraidas
df['setor'] = None
df['LPA'] = None
df['ROA'] = None
df['ROE'] = None
df['P/L'] = None
df['VPA'] = None

# Obter do site https://www.fundamentus.com.br/ as informações para cada ativo.
# Inicializa o o driver especificando o navegador de busca.
driver = webdriver.Chrome()

for i in df['Código']:
    
    try:        
        # Realiza a consulta no site para cada ativo.
        driver.get(f'https://www.fundamentus.com.br/detalhes.php?papel={i}')    

        # Obtem o valor do campo para cada classe de busca especificando a posição do objeto.
        preco = driver.find_elements(By.CLASS_NAME, 'txt')[3].text.replace(',', '.')
        setor = driver.find_elements(By.CLASS_NAME, 'txt')[13].text
        pl = driver.find_elements(By.CLASS_NAME, 'txt')[32].text
        lpa = driver.find_elements(By.CLASS_NAME, 'txt')[34].text
        vpa = driver.find_elements(By.CLASS_NAME, 'txt')[39].text
    
        # Salva a informação coletada no seu respectivo campo
        df.loc[df['Código'] == i, 'setor'] = setor          
        df.loc[df['Código'] == i, 'P/L'] = pl
        df.loc[df['Código'] == i, 'LPA'] = lpa
        df.loc[df['Código'] == i, 'VPA'] = vpa
    
        print(f'Obtendo dados para o ativo {i}')
        
    except:
        print(f'Erro ao obter os dados para o ativo {i}')

# Encerra o driver de pesquisa após a extração dos dados
driver.quit()
            
df.head()

# In[]
######################### Estatísticas Descritivas do Conjunto ########################################

# Verificando dados ausentes
df.isnull().sum()

# Informações sobre o conjunto de dados
df.info()

# Total de setores
total_setor = df['setor'].nunique()
total_setor

# Total de ativos por setor
total_ativos_setor = df['setor'].value_counts().sort_values(ascending=True)

plt.figure(figsize=(10, 7))
ax = total_ativos_setor.plot(kind='barh', color='skyblue', edgecolor='black')
plt.title('Total de Ativos por Setor', fontsize=16)
plt.xlabel('Número de Ativos', fontsize=12)
plt.ylabel('Setor', fontsize=12)
plt.show()
