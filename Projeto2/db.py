import mysql.connector

def Conectar():
    conexao = mysql.connector.connect(
        user = "seu user",
        password = "Sua senha",
        host = "Seu host",
        database = "Seu banco"
    )

    return conexao