from db import Conectar

def CriarCategoria(nome):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO categorias (nome) VALUES (%s)"
    cursor.execute(query, (nome, ))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Categoria criada"

def CriarProduto(nome, preco, estoque, ativo, categoria_id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO produtos (nome, preco, estoque, ativo, categoria_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome, preco, estoque, ativo, categoria_id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Produto criado"

def MostrarProdutos():
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("""SELECT 
    produtos.id,
    produtos.nome AS produto,
    produtos.preco,
    produtos.estoque,
    categorias.nome AS categoria
    FROM produtos
    JOIN categorias 
    ON produtos.categoria_id = categorias.categoria_id
    """)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    print("Query executada")
    return resultado

def AtualizarProdutos(preco, id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "UPDATE produtos SET preco = %s WHERE id = %s"
    cursor.execute(query, (preco, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Atualização concluida"
    
def ExcluirProdutos(id):
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    query = "DELETE FROM produtos WHERE id = %s"
    cursor.execute(query, (id, ))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Produto excluído"