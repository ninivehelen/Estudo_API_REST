from flask_restful import Resource

habilidades = ['Java','Php','Flask']

class lista_habilidades(Resource):
    def get(self):
        return habilidades

