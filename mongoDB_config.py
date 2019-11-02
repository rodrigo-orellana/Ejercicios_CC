from model import Jugador
from mongoDB import BaseDatos

import os

if(__name__ == "__main__"):
    # direccion = "mongodb://127.0.0.1:27017/MiBaseDatos"
    #direccion = "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/MiBaseDatos?retryWrites=true&w=majority"
    #direccion = "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/MiBaseDatos?ssl=true&ssl_cert_reqs=CERT_NONE"
    #direccion = "mongodb://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net:27017"
    direccion = "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/sample_airbnb?retryWrites=true&w=majority"
# 26018
#    client = pymongo.MongoClient(")
#db = client.test
# mongo = BaseDatos("mongodb://AlejandroCC:" + os.environ.get('MLABPASS') +
    #
    #
    #     "@ds026018.mlab.com:26018/jugadores", True)

j1 = Jugador("Hapneck", "Alejandro", "Campoy Nieves", 22, [
    "Fortnite", "Hollow Knight", "The Witcher"], True)
j2 = Jugador("Malcaide", "Alfonso", "Barragan Lara",
             22, ["Counter Strike"], True)
j3 = Jugador("Rekkles", "Juan", "Martinez Casado", 22, [
    "Fortnite", "League of Legends", "Counter Strike"], False)

mongo = BaseDatos(direccion, False)

mongo.insertJugador(j1)
mongo.insertJugador(j2)
mongo.insertJugador(j3)
