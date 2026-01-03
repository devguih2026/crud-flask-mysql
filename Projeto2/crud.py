from db import Conectar

def NovoFuncionario(nome, data_nascimento, cargo, setor, data_admissao):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO funcionarios (nome, data_nascimento, cargo, setor, data_admissao) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome, data_nascimento, cargo, setor, data_admissao))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Query executada"
    
def MostrarFuncionarios():
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM funcionarios")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    print("Query executada")
    return resultado

def RemoverFuncionarios(id):
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    query = "DELETE FROM funcionarios WHERE id = %s"
    cursor.execute(query, (id, ))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Query executada"

def AtualizarFuncionarios(cargo, id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "UPDATE funcionarios SET cargo = %s WHERE id= %s"
    cursor.execute(query, (cargo, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Dados atualizados"
    
