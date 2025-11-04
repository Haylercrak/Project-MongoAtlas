from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os
# cargar variables de entorno
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI_ATLAS")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

try:
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    print("Conexión exitosa a la base de datos MongoDB Atlas")
    
except :
    print(f"Error al conectar a la base de datos:")