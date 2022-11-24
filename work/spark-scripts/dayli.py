from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from datetime import datetime
from datetime import timedelta
from mongoDbConnection import instert_data
import json


spark = SparkSession.builder.getOrCreate()
def return_good_format(val):
    if len(str(val)) == 1:
        return '0'+str(val)
    else:
        return str(val)

start_date = datetime.now()+timedelta(days= -1)

_y = return_good_format(start_date.year)
_m = return_good_format(start_date.month)
_d = return_good_format(start_date.day)

crypto_list = [
    'BNBBUSD',
    'ETHBUSD',
    'BTCBUSD',
    'AVAXBUSD',
    'MATICBUSD',
    'SOLBUSD'
]

schema = StructType() \
            .add("timestamp",StringType(),True) \
            .add("open",FloatType(),True) \
            .add("high",FloatType(),True) \
            .add("low",FloatType(),True) \
            .add("close",FloatType(),True) \
            .add("volume",FloatType(),True) \
            .add("close_time",StringType(),True) \
            .add("quote_asset_volume",FloatType(),True) \
            .add("number_of_trades",IntegerType(),True) \
            .add("taker_buy_base_asset_volume",FloatType(),True) \
            .add("taker_buy_quote_asset_volume",FloatType(),True) \
            .add("ignore",IntegerType(),True)

for crypto in crypto_list:

    file_name = crypto+'-4h-'+_y+'-'+_m+'-'+_d

    path = "hdfs://localhost:9000/data/"+file_name
        
    df_binance = spark.read.format("csv") \
        .option("header", False) \
        .schema(schema) \
        .load(path)


    df_binance = df_binance.withColumn("_id", col("timestamp"))

    json_data = df_binance.toJSON(use_unicode=True).map(lambda j: json.loads(j)).collect()

    instert_data(crypto, json_data)
