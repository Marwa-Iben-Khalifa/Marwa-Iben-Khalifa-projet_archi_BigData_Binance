import os
import dotenv
from pymongo import MongoClient
import pandas as pd
dotenv.load_dotenv()
pwd = os.getenv('dbPassword')

client = MongoClient("mongodb+srv://hicham:"+pwd+"@hichamcluster.q07np.mongodb.net/?retryWrites=true&w=majority")
print("Connection Successful")



mydb = client["projectDB"]


def get_all_data(coin):
    mycol = mydb[coin]
    result = mycol.find()
    df = pd.DataFrame(list(result))
    df.drop(columns=['_id', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'], axis=1, inplace=True)
    df = df.astype({'timestamp': 'int'})
    df = df.reindex(columns = ['timestamp','open','high', 'low', 'close'])
    df.sort_values(by=["timestamp"], inplace = True)
    print(df.dtypes)
    return df.to_json(orient="split")

dblist = client.list_database_names()
collist = mydb.list_collection_names()
if "projectDB" in dblist:
    print("The database exists.")
if "csv" in collist:
    print("The collection exists.")
#client.close()
