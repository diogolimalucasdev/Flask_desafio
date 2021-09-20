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
@app.route('/registro/<int:id>/', methods=['GET', 'PUT', 'POST'])
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
                print(lista[0])
                if dados['id'] == lista[0] and dados['responsavel'] == lista[1] and dados['tarefa'] == lista[2]:
                    tarefas[id - 1] = dados
                    print(tarefas)
                    return jsonify(dados)
                else:
                    print("nao foi")

            else:
                return "Login nao identificado"
    elif request.method == 'POST':
        dados = json.loads(request.data)

        for valor in tarefas:
            identificador, responsavel, tarefa, status = valor.values()

            if id == identificador:
                return "Id ja cadastrado"
            else:
                return tarefas.append(dados)


@app.route('/registro/<int:id>/deletar/', methods=['DELETE'])
def deletar(id):
    tarefas.pop(id)
    return jsonify({'status': 'sucesso', 'mensagem': 'Tarefa excluida'})


if __name__ == '__main__':
    app.run(debug=False)
