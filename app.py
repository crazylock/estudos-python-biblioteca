from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
       'id': 1,
       'titulo': 'o senhor dos anais',
       'autor': 'meu pau'
    },
    {
        'id': 2,
        'titulo': 'a poderosa tora',
        'autor': 'janequine'

    },
]

#consultar todos
@app.route('/livros')
def obter_livros ():
    return jsonify(livros)

#run
app.run(port=5000,host='localhost',debug=True)