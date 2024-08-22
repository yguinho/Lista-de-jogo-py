from flask import Flask, request, render_template, redirect

app = Flask(__name__)

game = []

@app.route("/")
def index():
    return render_template('index.html', game=game)


@app.route("/inserir", methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        # Lida com o envio do formulário de cadastro de jogo
        codigo = len(game)
        name = request.form['nome-jogo']
        genero = request.form['genero']
        tamanho = request.form['tamanho']
        game.append({'name': name, 'genero': genero, 'tamanho': tamanho, 'codigo': codigo})
        return redirect('/')

    # Renderiza a página de inserção
    return render_template('inserir.html')

@app.route("/editar/<int:codigo>", methods=['GET', 'POST'])
def editar(codigo):
    if request.method == 'POST':
        # Lida com o envio do formulário para editar um jogo
        name = request.form['nome-jogo']
        genero = request.form['genero']
        tamanho = request.form['tamanho']
        game[codigo] = {'name': name, 'genero': genero, 'tamanho': tamanho, 'codigo': codigo}
        return redirect('/')
    else:
        # Renderiza a página de edição com o jogo específico
        games = game[codigo]
        return render_template('inserir.html', game=games)

@app.route("/apagar/<int:codigo>")
def apagar(codigo):
    del game[codigo]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
