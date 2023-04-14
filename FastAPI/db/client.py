### MongoDB client ###

# Descarga version comunity: https://www.mongodb.com/try/download
# Instalacion: instalar los MSI que descargues
# Modulo conexion MongoDB: pip install pymongo
# Ejecucion: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# conexion: mongodb://localhost
# descargar la extesion mongodb en VSC


from pymongo import MongoClient

# Base de datos local
#db_client = MongoClient().local

# Base de datos Remota
# el ultimo .test es como quiero que se llame, puede tener cualquier nombre
db_client = MongoClient(
    "mongodb+srv://test:test@cluster1.cbqbk0w.mongodb.net/?retryWrites=true&w=majority").test







