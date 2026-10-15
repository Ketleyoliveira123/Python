# %%
"""
Create table Categoria(
ID int,
Categoria nvarchar(255)
)

"""

# %%

import pandas as pd
import pyodbc

server = 'KETLEY'
database = 'Python'

conexaoDB = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)

cursor = conexaoDB.cursor()

# %%
dados = pd.read_excel(r"C:\Users\Ketle\OneDrive\Documentos\Py_dados\Origem\arquivos_excel\Categoria.xlsx")
str(dados.columns).replace("'","") 






# %%
cursor.execute('truncate table [Categoria]')   #executa tarefa de  apagar dados
cursor.commit()

# %%
for index, linha in dados.iterrows():
    
    cursor.execute("Insert into [Categoria](ID,Categoria)values(?,?)",linha.id,linha.nome) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server
cursor.close()    #Fechar Cursor
conexaoDB.close() #Fechar Conexao

# %% [markdown]
# 


