from flask import Blueprint, request, jsonify
from crud import CriarUsuario
from werkzeug.security import check_password_hash, generate_password_hash


projeto_bp = Blueprint("projeto_bp", __name__)

@projeto_bp.route("/blog", methods=["POST"])
def NovoUsuario():
    dados= request.json

    nome = dados["nome"]
    email = dados["email"]
    senha = dados["senha"]
    senha_hash = generate_password_hash(senha)

    chamar = CriarUsuario(nome, email, senha_hash)
    return jsonify(chamar)
