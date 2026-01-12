import mysql.connector

def Conectar():
    conexao = mysql.connector.connect(
        user = "root",
        password = "Guilherme!",
        database = "blog",
        host = "localhost"
    )

    return conexao