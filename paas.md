## Ejercicios Tema 3    
**Ejercicio 1:**  
Darse de alta en algún servicio PaaS tal como Heroku, Nodejitsu, BlueMix u OpenShift.
![eje3.1](img/3.1.png "3.1") 

**Ejercicio 2:**  
Crear una aplicación en OpenShift o en algún otro PaaS en el que se haya dado uno de alta. Realizar un despliegue de prueba usando alguno de los ejemplos. 



**Ejercicio 3:**  
Realizar una app en express (o el lenguaje y marco elegido) que incluya variables como en el caso anterior.
~~~
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from desafio import Desafio
from mongoDB import BaseDatos
import logging
import datetime

app = Flask("ecochallenge")
api = Api(app)

logging.basicConfig(filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,  datefmt='%d-%b-%y %H:%M:%S'

mongo = BaseDatos(
        "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/desafio?retryWrites=true&w=majority", False)
parser = reqparse.RequestParser()
parser.add_argument('nombre', type=str,
                    help='desafío no puede ser null', required=True)
parser.add_argument('fecha_ini', type=datetime, required=True)
parser.add_argument('fecha_fin', type=datetime, required=True)
parser.add_argument('pais', type=str, required=False)
parser.add_argument('ciudad', type=str, required=False)


def abortar_ruta_inexistente(ruta):
    if(False):  # Crear validación
        abort(404, message="Error 404. La ruta {} no existe".format(ruta))

class Principal(Resource):
    def get(self):
        return {'status': 'OK'}


class DesafioIndividual(Resource):
    def get(self, ruta):
        abortar_ruta_inexistente(ruta)
        logging.info("Obteniendo desafios de la base de datos.")
        return {ruta: mongo.getDesafio(ruta)}

    def put(self, ruta):
        args = parser.parse_args()
        desafio = Desafio(args['Nombre'], args['Fecha_ini'], args['Fecha_fin'])
        exito = mongo.insertDesafio(desafio)
        if(not(exito)):
            mongo.updateDesafio(args['Nombre'], desafio.__dict__())
        return mongo.getDesafio(ruta)

    def delete(self, ruta):
        mongo.removeDesafio(ruta)
        return '', 204


class Desafios(Resource):

    def get(self):
        return mongo.getDesafios()

    def post(self):
        args = parser.parse_args()
        desafio = Desafio(args['Nombre'], args['Fecha_ini'], args['Fecha_fin'])
        ruta = args['Nombre']
        mongo.insertDesafio(desafio)
        return mongo.getDesafio(ruta), 201

    def delete(self):
        mongo.removeDesafios()
        return '', 204


api.add_resource(Principal, '/', '/status')
api.add_resource(Desafios, '/desafios')
api.add_resource(DesafioIndividual, '/desafios/<string:ruta>')


if (__name__ == '__main__'):
    # Esto es para que pueda abrirse desde cualquier puerto y
    #  direccion(de esta forma en heroku no nos da error).
    port = int(os.environ.get("PORT", 8989))
    app.run(host="0.0.0.0", port=port, debug=False)
~~~

**Ejercicio 4:**  
Crear pruebas para las diferentes rutas de la aplicación.


**Ejercicio 5:**  
Instalar y echar a andar tu primera aplicación en Heroku.

![eje3.4.1](img/3.4.1.png "3.4.1") 
![eje3.4.2](img/3.4.2.png "3.4.2") 

**Ejercicio 6:**  

**Ejercicio 7:**  
Haz alguna modificación a tu aplicación en para Heroku, sin olvidar añadir los tests para la nueva funcionalidad, Despliegue automático a Heroku 



**Ejercicio 8:**  
Preparar la aplicación con la que se ha venido trabajando hasta este momento para ejecutarse en un PaaS, el que se haya elegido.