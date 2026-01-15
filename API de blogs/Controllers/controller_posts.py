from flask import Blueprint, request, jsonify
from crud.crud_posts import NovoPost, MostrarPosts, AtualizarPosts, ApagarPosts, ValidarAutor

posts_bp = Blueprint("posts_bp", __name__)

@posts_bp.route("/blog/posts", methods=["POST"])
def CriarPost():
    dados = request.json

    titulo = dados["titulo"]
    conteudo = dados["conteudo"]
    id_usuario = dados["id_usuario"]

    chamar = NovoPost(titulo, conteudo, id_usuario)
    return jsonify(chamar)

@posts_bp.route("/blog/posts", methods=["GET"])
def ListarPosts():
    chamar = MostrarPosts()
    return chamar

@posts_bp.route("/blog/posts/<id>", methods=["PUT"])
def Atualizar(id):
    dados= request.json

    titulo = dados["titulo"]
    chamar = AtualizarPosts(titulo, id)
    return jsonify(chamar)

@posts_bp.route("/blog/posts/<int:id_posts>/usuario/<int:id_usuario>", methods=["DELETE"])
def DeletarPost(id_posts, id_usuario):

    # verifica se esse post pertence a esse usuário
    autor = ValidarAutor(id_posts, id_usuario)

    if not autor:
        return jsonify({"erro": "Você não é o autor deste post"}), 403

    chamar = ApagarPosts(id_posts)
    return jsonify(chamar), 200


