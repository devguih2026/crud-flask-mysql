from flask import Blueprint, request, jsonify
from crud.crud_usuarios import CriarUsuario, VerUsuarios, AlterarDadosUsuario, ApagarUsuario
from crud.crud_posts import NovoPost
from werkzeug.security import check_password_hash, generate_password_hash

usuarios_bp = Blueprint("usuarios_bp", __name__)

@usuarios_bp.route("/blog/usuario", methods=["POST"])
def NovoUsuario():
    dados= request.json

    nome = dados["nome"]
    email = dados["email"]
    senha = dados["senha"]
    senha_hash = generate_password_hash(senha)

    chamar = CriarUsuario(nome, email, senha_hash)
    return jsonify(chamar)

@usuarios_bp.route("/blog", methods=["GET"])
def ListarUsuarios():
    chamar = VerUsuarios()
    return chamar

@usuarios_bp.route("/blog/usuario/<id>", methods=["PUT"])
def NovoNome(id):
    dados= request.json

    nome = dados["nome"]
    chamar = AlterarDadosUsuario(nome, id)
    return jsonify(chamar)

@usuarios_bp.route("/blog/usuario/<id_usuario>", methods=["DELETE"])
def DeletarUsuario(id):
    chamar = ApagarUsuario(id)
    return jsonify(chamar)


