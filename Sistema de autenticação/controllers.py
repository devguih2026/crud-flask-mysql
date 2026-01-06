from flask import Blueprint, request, jsonify
from crud import Cadastrar, MostrarUsuarios, RemoverUsuario, AtualizarUsuario, BuscarUsuarioPorEmail
from werkzeug.security import check_password_hash, generate_password_hash

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
    senha_hash = generate_password_hash(senha)

    if not nome or not email or not senha:
        return jsonify({"erro": "Campos não podem estar vazios"}), 400 # valida se nome, email ou senha foram preenchidos
    
    if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(senha, str):
        return jsonify({"erro": "Tipo de dado inválido"}), 400 # valida se os tipos de dados estão corretos

    chamar = Cadastrar(nome, email, senha_hash)

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


@projeto_bp.route("/login", methods=["POST"])
def Login():
    dados = request.json
   # senha_hash = generate_password_hash(senha)


    # 1. validar JSON
    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400

    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400

    # 2. buscar usuário
    usuario = BuscarUsuarioPorEmail(email)

    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    # 3. validar senha
    if not check_password_hash(usuario["senha"], senha):
        return jsonify({"erro": "Senha inválida"}), 401

    # 4. login válido
    return jsonify({
        "mensagem": "Login realizado com sucesso",
        "id": usuario["id"],
        "nome": usuario["nome"],
        "email": usuario["email"]
    }), 200


