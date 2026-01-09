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

def AtualizarProdutos():
    conexao = Conectar()
    cursor = conexao.cursor()
    

def ExcluirProdutos():
    conexao = Conectar()
    cursor = conexao.cursor()