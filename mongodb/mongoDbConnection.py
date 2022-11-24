from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://hicham:1FDA2LrFuNnJgCWD@hichamcluster.q07np.mongodb.net/?retryWrites=true&w=majority")
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
