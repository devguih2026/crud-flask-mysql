from db import Conectar

def NovoPost(titulo, conteudo, id_usuario):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO posts (titulo, conteudo, id_usuario) VALUES (%s, %s, %s)"
    cursor.execute(query, (titulo, conteudo, id_usuario))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Post criado"

def MostrarPosts():
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(""" SELECT 
    posts.id_posts,
    posts.titulo,            
    posts.conteudo,               
    usuario.nome AS usuario               
    FROM posts               
    JOIN usuario               
    ON posts.id_usuario = usuario.id_usuario """)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def AtualizarPosts(titulo, id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "UPDATE posts SET titulo = %s WHERE id_posts = %s"
    cursor.execute(query, (titulo, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Titulo alterado"

def ApagarPosts(id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "DELETE FROM posts WHERE id_posts = %s"
    cursor.execute(query, (id, ))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "post removido"

def ValidarAutor(id_posts, id_usuario):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = """
        SELECT id_posts
        FROM posts
        WHERE id_posts = %s AND id_usuario = %s
    """
    cursor.execute(query, (id_posts, id_usuario))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

