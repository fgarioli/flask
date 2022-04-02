from flask_classful import FlaskView, route


class CacaView(FlaskView):
    route_base = '/xixi'

    def index(self):
        return "<br>"

    @route('/teste', methods=['GET'])
    @route('/teste/<id>', methods=['GET'])
    def teste(self, id: int = None):
        return id if id else 'teste'

    # @app.route('/', methods=['GET', 'POST'])
    # def form():
    #     if request.method == 'POST':
    #         nome = request.form.get('fname')
    #         sobrenome = request.form.get('lname')
    #         return f"Seu nome é {nome} {sobrenome}"
    #     return render_template("form.html")
