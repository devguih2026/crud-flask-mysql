from flask import Blueprint, request, jsonify
from crud import Cadastrar, MostrarUsuarios, RemoverUsuario, AtualizarUsuario

projeto_bp = Blueprint("projeto_bp", __name__)

@projeto_bp.route("/instagram", methods=["POST"])
def NovoUsario():
    dados = request.json

    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400 # valida se o JSON foi enviado
    
    if "email" not in dados or "senha" not in dados or "nome" not in dados:
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400 # valida se email, senha ou nome existem

    nome = dados["nome"]
    email = dados["email"]
    senha = dados["senha"]

    if not nome or not email or not senha:
        return jsonify({"erro": "Campos não podem estar vazios"}), 400 # valida se nome, email ou senha foram preenchidos
    
    if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(senha, str):
        return jsonify({"erro": "Tipo de dado inválido"}), 400 # valida se os tipos de dados estão corretos

    chamar = Cadastrar(nome, email, senha)

    return jsonify(chamar), 201

@projeto_bp.route("/instagram", methods=["GET"])
def VerUsuarios():
    chamar = MostrarUsuarios()
    return jsonify(chamar), 200

@projeto_bp.route("/instagram/usuario/<id>", methods=["PUT"])
def AtualizarDados(id):
    dados = request.json
    nome = dados["nome"]
    chamar = AtualizarUsuario(nome, id)
    return jsonify(chamar)

@projeto_bp.route("/instagram/usuario/<id>", methods=["DELETE"])
def ApagarUsuario(id):
    chamar = RemoverUsuario(id) 
    return jsonify(chamar)


