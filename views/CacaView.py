from flask import redirect, render_template, request
from flask_classful import FlaskView, route
import dao


class CacaView(FlaskView):
    route_base = '/'

    def index(self):
        return "<br>"

    @route('/alterar/<int:id>', methods=['POST'])
    @route('/cadastrar', methods=['POST'])
    def cadastrar(self, id: int = None):
        if id:
            dao.editar(dict(request.form))
        else:
            dao.adicionar(dict(request.form))
        return redirect("/listar")

    @route('/deletar/<int:id>', methods=['GET'])
    def deletar(self, id: int):
        dao.deletar(id)
        return redirect("/listar")

    @route('/cadastro/<int:id>', methods=['GET'])
    @route('/cadastro', methods=['GET'])
    def form(self, id: int = None):
        if id:
            print(dao.selecionar(id))
            return render_template("form.html", dados=dao.selecionar(id))

        return render_template("form.html")

    @route('/listar', methods=['GET'])
    def listar(self):
        return render_template("listar.html", lista=dao.selecionarTodos())
