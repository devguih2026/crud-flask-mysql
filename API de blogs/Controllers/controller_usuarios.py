from flask import Blueprint, request, jsonify
from crud.crud_usuarios import CriarUsuario, VerUsuarios, AlterarDadosUsuario, ApagarUsuario
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

@projeto_bp.route("/blog", methods=["GET"])
def ListarUsuarios():
    chamar = VerUsuarios()
    return chamar

@projeto_bp.route("/blog/usuario/<id>", methods=["PUT"])
def NovoNome(id):
    dados= request.json

    nome = dados["nome"]
    chamar = AlterarDadosUsuario(nome, id)
    return jsonify(chamar)

@projeto_bp.route("/blog/usuario/<id>", methods=["DELETE"])
def DeletarUsuario(id):
    chamar = ApagarUsuario(id)
    return jsonify(chamar)
