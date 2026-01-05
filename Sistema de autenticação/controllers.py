from flask import Blueprint, request, jsonify
from crud import Cadastrar

projeto_bp = Blueprint("projeto_bp", __name__)

@projeto_bp.route("/instagram", methods=["POST"])
def NovoUsario():
    dados = request.json

    nome = dados["nome"]
    email = dados["email"]
    senha = dados["senha"]

    chamar = Cadastrar(nome, email, senha)

    return jsonify(chamar), 201