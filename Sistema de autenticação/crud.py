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

def MostrarUsuarios():
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def AtualizarUsuario(nome, id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "UPDATE usuario SET nome = %s WHERE id = %s"
    cursor.execute(query, (nome, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Dados atualizados"

def RemoverUsuario(id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "DELETE FROM usuario WHERE id = %s"
    cursor.execute(query, (id, ))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Usuário removido"