import mysql.connector

def Conectar():
    cnx = mysql.connector.connect(
        user = "Seu user",
        password = "Sua senha",
        host ="Seu host",
        database = "Seu banco"
    )

    return cnx