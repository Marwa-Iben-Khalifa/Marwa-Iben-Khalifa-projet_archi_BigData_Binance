import os
import dotenv
from pymongo import MongoClient
dotenv.load_dotenv()
pwd = os.getenv('dbPassword')

client = MongoClient("mongodb+srv://hicham:"+pwd+"@hichamcluster.q07np.mongodb.net/?retryWrites=true&w=majority")
print("Connection Successful")



mydb = client["projectDB"]
def instert_data(coin, data):
    mycol = mydb[coin]
    mycol.insert_many(data)


dblist = client.list_database_names()
collist = mydb.list_collection_names()
if "projectDB" in dblist:
    print("The database exists.")
if "csv" in collist:
    print("The collection exists.")
#client.close()
