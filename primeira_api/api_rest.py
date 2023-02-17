from flask import Flask, request
from flask_restful import Resource , Api
from habilidades import lista_habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':'0',
     'Nome':'Junior',
     'Habilidade':['python', 'Django']},

    { 'id':'1',
     'Nome':'Claudia',
     'Habilidade':['Java', 'Flask']}
]

class desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'desenvolvedor do id':id,'mensagem':'não existe'}
        except Exception:
            response = {'mensagem':'erro desconhecido'}
        return response

    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] =  dados
        return dados
    
    def delete(self,id):
        desenvolvedores.pop(id)
        return ({'status':'sucesso','mensagem':'registro excluído'})

class lista_desenvolvedores(Resource): 
     def get(self):      
         return (desenvolvedores)

     def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return ({'status':'sucesso','mensagem':'registro inserido'})

api.add_resource(desenvolvedor, '/dev/<int:id>')
api.add_resource(lista_desenvolvedores, '/dev/')
api.add_resource(lista_habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run()