from flask import Blueprint, request, jsonify
from crud import CriarCategoria, CriarProduto, MostrarProdutos, AtualizarProdutos, ExcluirProdutos

projeto_bp = Blueprint("projeto_bp", __name__)

@projeto_bp.route("/americanas/categoria", methods=["POST"])
def NovaCategoria():
    dados = request.json
    nome = dados["nome"]

    chamar = CriarCategoria(nome)
    return jsonify(chamar)

@projeto_bp.route("/americanas/produtos", methods=["POST"])
def NovoProduto():
    dados = request.json

    nome = dados["nome"]
    preco = dados["preco"]
    estoque = dados["estoque"]
    ativo = dados["ativo"]
    categoria_id = dados["categoria_id"]

    chamar = CriarProduto(nome, preco, estoque, ativo, categoria_id)
    return jsonify(chamar)

@projeto_bp.route("/americanas", methods=["GET"])
def ListarTudo():
    chamar = MostrarProdutos()
    return jsonify(chamar)