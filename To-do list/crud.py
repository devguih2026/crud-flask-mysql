from db import Conectar

def NovaTarefa(idiomas, anki, tecnologia, subir_github, entretenimento, horas, tudo_concluido):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO lista (idiomas, anki, tecnologia, subir_github, entretenimento, horas, tudo_concluido) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (idiomas, anki, tecnologia, subir_github, entretenimento, horas, tudo_concluido))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Query executada"

def ListarTarefas():
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM lista")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    print("Query executada")
    return resultado

def AtualizarTarefas(tecnologia, id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "UPDATE lista SET tecnologia = %s WHERE id= %s"
    cursor.execute(query, (tecnologia, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Dados atualizados"

def RemoverTarefa(id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "DELETE FROM lista WHERE id = %s"
    cursor.execute(query, (id, ))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Query executada"
