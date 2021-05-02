import os
import dotenv
from pymongo import MongoClient
import dns

dotenv.load_dotenv()

dburl = os.getenv("URL")

print(dburl)
if not dburl:
    raise ValueError("no tienes url mongodb")

#Vamos a conectar con la base de datos
client = MongoClient("mongodb+srv://dbuser:api2021@cluster0.q59hz.mongodb.net/API")
db = client.get_database()
collection = db["quotes"]
