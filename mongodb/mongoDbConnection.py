import os
import dotenv
from pymongo import MongoClient
dotenv.load_dotenv()
pwd = os.getenv('dbPassword')

client = MongoClient(
    f"mongodb+srv://hicham:{pwd}@hichamcluster.q07np.mongodb.net/?retryWrites=true&w=majority")
print("Connection Successful")


mydb = client["projectDB"]
dblist = client.list_database_names()
mycol = mydb["csv"]
collist = mydb.list_collection_names()
if "projectDB" in dblist:
    print("The database exists.")
if "csv" in collist:
    print("The collection exists.")
client.close()
