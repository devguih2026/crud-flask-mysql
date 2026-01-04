from flask import Blueprint, request, jsonify
from crud import NovaTarefa, ListarTarefas, AtualizarTarefas, RemoverTarefa

projeto_bp = Blueprint("projeto_bp", __name__)

@projeto_bp.route("/tarefas", methods=["POST"])
def NovasTarefas():
    dados = request.json

    """idiomas = dados["idiomas"]
    anki = dados["anki"]
    tecnologia = dados["tecnologia"]
    subir_github = dados["subir_github"]
    entretenimento = dados["entretenimento"]
    horas = dados["horas"]
    tudo_concluido = dados["tudo_concluido"]
  
    chamar = NovaTarefa(idiomas, anki, tecnologia, subir_github, entretenimento, horas, tudo_concluido)

    return jsonify(chamar), 201"""

@projeto_bp.route("/tarefas", methods=["GET"])
def VerTarefas():
    chamar = ListarTarefas()
    return jsonify(chamar), 200

@projeto_bp.route("/tarefas/lista/<id>", methods=["DELETE"])
def ApagarTarefa(id):
    chamar = RemoverTarefa(id) 
    return jsonify(chamar)

@projeto_bp.route("/tarefas/lista/<id>", methods=["PUT"])
def Atualizar(id):
    dados = request.json
    tecnologia = dados["tecnologia"]
    chamar = AtualizarTarefas(tecnologia, id)
    return jsonify(chamar)
