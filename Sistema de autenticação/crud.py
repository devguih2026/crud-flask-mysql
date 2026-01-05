from db import Conectar

def Cadastrar(nome, email, senha):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, email, senha))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Usuário cadastrado"
