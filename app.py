from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nome = request.form.get('fname')
        sobrenome = request.form.get('lname')
        return f"Seu nome é {nome} {sobrenome}"
    return render_template("form.html")


if __name__ == '__main__':
    app.run()