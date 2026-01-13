from db import Conectar

def CriarUsuario(nome, email, senha):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, email, senha))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Usuário criado"

def VerUsuarios():
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def AlterarDadosUsuario(nome, id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "UPDATE usuario SET nome = %s WHERE id_usuario = %s"
    cursor.execute(query, (nome, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Nome alterado"

def ApagarUsuario(id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "DELETE FROM usuario WHERE id_usuario = %s"
    cursor.execute(query, (id, ))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Usuário removido"
