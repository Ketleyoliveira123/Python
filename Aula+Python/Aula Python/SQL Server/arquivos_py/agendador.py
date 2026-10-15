import schedule
import time
import pandas as pd
import pyodbc


def job():

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

    dados = pd.read_excel(
        r"C:\Users\Ketle\OneDrive\Documentos\Py_dados\Origem\arquivos_excel\Categoria.xlsx"
    )

    dados.columns = dados.columns.str.strip()

    print(dados.columns)

    for index, linha in dados.iterrows():

        cursor.execute(
            "INSERT INTO Categoria (ID, Categoria) VALUES (?, ?)",
            linha["id"],
            linha["Nome"]
        )

    conexaoDB.commit()

    cursor.close()
    conexaoDB.close()


schedule.every(10).seconds.do(job) #  a cada 10 segundos va executar a função job

while True:
    schedule.run_pending()
    time.sleep(1) # o tempo de espera para executar a função job a cada 10 segundos, mas o loop vai rodar a cada 1 segundo para verificar se tem alguma tarefa pendente.
    

