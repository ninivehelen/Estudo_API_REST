from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {'id':'0',
     'Nome':'Junior',
     'Habilidade':['python', 'Django']},

    { 'id':'1',
     'Nome':'Claudia',
     'Habilidade':['Java', 'Flask']}
]

@app.route('/dev/<int:id>/', methods= ['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'desenvolvedor do id':id,'mensagem':'não existe'}
        except Exception:
            response = {'mensagem':'erro desconhecido'}
    
        return jsonify(response)

    elif request.method == 'PUT':
         dados = json.loads(request.data)
         desenvolvedores[id] =  dados
         return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'registro excluído'})

@app.route('/dev/',  methods=['POST', 'GET'])
def lista_desenvolvedores():
    if(request.method =='POST'):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return  jsonify({'status':'sucesso','mensagem':'registro inserido'})

    elif(request.method =='GET'):
        return jsonify(desenvolvedores)

    # elif(request.method =='POST'):

if __name__ == '__main__':
    app.run()