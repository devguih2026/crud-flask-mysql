import mysql.connector

def Conectar():
    conexao = mysql.connector.connect(
        user = "root",
        database = "instagram",
        password = "Guilherme!",
        host = "localhost"
    )

    return conexao