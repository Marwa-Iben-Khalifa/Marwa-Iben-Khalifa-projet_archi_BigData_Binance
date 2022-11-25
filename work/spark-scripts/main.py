from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from mongoDbConnection import instert_data
import json


spark = SparkSession.builder.getOrCreate()

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

      path = "hdfs://localhost:9000/data/"+crypto+"*"
            
      df_binance = spark.read.format("csv") \
            .option("header", False) \
            .schema(schema) \
            .load(path)


      df_binance = df_binance.withColumn("_id", col("timestamp"))


      partirioned_by_id = Window.orderBy("timestamp")

      @udf(returnType = FloatType())
      def sma(oldmin, old, new):
            if not oldmin == None:
                  return ((oldmin + old + new) / 3)
            else:
                  return 0
                  
      @udf(returnType = FloatType())
      def sma_louche(oldmin, new):
            if not oldmin == None:
                  return ((oldmin + new) / 2)
            else:
                  return 0

     # df_binance = df_binance.withColumn("_id", col("timestamp"))

      df_binance = df_binance.withColumn("sma", sma(F.lag("close", offset=2).over(partirioned_by_id), F.lag("close", offset=1).over(partirioned_by_id), F.lag("close", offset=0).over(partirioned_by_id)))

      df_binance = df_binance.withColumn("smaLouche", sma_louche(F.lag("close", offset=24).over(partirioned_by_id), F.lag("close", offset=0).over(partirioned_by_id)))

      json_data = df_binance.toJSON(use_unicode=True).map(lambda j: json.loads(j)).collect()

      instert_data(crypto, json_data)
