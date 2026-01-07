import mysql.connector

def Conectar():
    conexao = mysql.connector.connect(
        user = "root",
        host = "localhost",
        database = "americanas",
        password = "Guilherme!"
    )

    return conexao