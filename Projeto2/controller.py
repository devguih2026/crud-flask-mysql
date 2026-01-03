from flask import Blueprint, request, jsonify
from crud import NovoFuncionario, MostrarFuncionarios, RemoverFuncionarios, AtualizarFuncionarios

projeto_bp = Blueprint("projeto_bp", __name__)

@projeto_bp.route("/empresa", methods=["POST"])
def NovoDado():
    dados = request.json

    nome = dados["nome"]
    data_nascimento = dados["data_nascimento"]
    cargo = dados["cargo"]
    setor = dados["setor"]
    data_admissao = dados["data_admissao"]

    chamar = NovoFuncionario(nome, data_nascimento, cargo, setor, data_admissao)

    return jsonify(chamar), 201

@projeto_bp.route("/empresa", methods=["GET"])
def VerDados():
    chamar = MostrarFuncionarios()
    return jsonify(chamar), 200

@projeto_bp.route("/empresa/funcionarios/<id>", methods=["DELETE"])
def ApagarDados(id):
    chamar = RemoverFuncionarios(id) 
    return jsonify(chamar)

@projeto_bp.route("/empresa/funcionarios/<id>", methods=["PUT"])
def Atualizacao(id):
    dados = request.json
    cargo = dados["cargo"]
    chamar = AtualizarFuncionarios(cargo, id)
    return jsonify(chamar)