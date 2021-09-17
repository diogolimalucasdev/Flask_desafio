from flask import Flask, request, jsonify
import json
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
tarefas = [
    {
        "id": 1,
        "responsavel": "Diogo",
        "tarefa": "Estudar",
        "status": "Fazendo"
    },
    {
        "id": 2,
        "responsavel": "Maria",
        "tarefa": "Trabalhar",
        "status": "Fazendo"
    },
    {
        "id": 3,
        "responsavel": "Miguel",
        "tarefa": "Estudar",
        "status": "Descansando"
    }
]


def verificar():
    for resultado in tarefas:
        id, responsavel, tarefa, status = resultado.values()
        if id == 1:
            dados = id, responsavel, tarefa
            id2 = 1
            responsavel = "Diogo"
            tarefa2 = "Estudar"
            if id2 == dados[0] and responsavel == dados[1] and tarefa2 == dados[2]:
                print("foi")


verificar()


@app.route('/')
def testar():
    return "esta funcionando"


# aqui eu retorno todas as tarefas, de todos que estao cadastrados
@app.route('/registro', methods=['GET'])
def registro():
    # verifico se minha requisição é do tipo 'GET' se for eu mostro
    if request.method == 'GET':
        return jsonify(tarefas)
    else:
        return "sem acesso"


# aqui eu retorno a tarefa individual chamada por cada ID
@app.route('/registro/<int:id>/', methods=['GET', 'PUT'])
def registro_pessoal(id):
    if request.method == 'GET':
        tarefas_pessoal = tarefas[id - 1]
        return jsonify(tarefas_pessoal)
    elif request.method == 'PUT':
        # pego o que ta sendoescrito no meu body o json.loads E o método loads, assim como o dumps, é para lidar com
        # JSON em formato de string. No caso do loads, transformar uma string em um objeto Python.
        dados = json.loads(request.data)
        print(dados)

        # estou fazendo uma verificação se o que foi mudado foi somente o status
        # se caso tentar mudar, tarefa, responsavel ou id ele nao vai deixar

        for valor in tarefas:
            identificador, responsavel, tarefa, status = valor.values()

            if id == identificador:
                lista = identificador, responsavel, tarefa
                if dados['id'] == lista[0] and dados['responsavel'] == lista[1] and dados['tarefa'] == lista[2]:
                    print(jsonify(dados))


if __name__ == '__main__':
    app.run(debug=False)
