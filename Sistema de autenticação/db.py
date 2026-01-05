import mysql.connector

def Conectar():
    conexao = mysql.connector.connect(
        user = "Seu user",
        database = "Seu banco",
        password = "Sua senha",
        host = "Seu host"
    )

    return conexao