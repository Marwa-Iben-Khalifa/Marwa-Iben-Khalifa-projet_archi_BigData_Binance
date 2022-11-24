from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.getOrCreate()

path = "hdfs://localhost:9000/data/BNBBUSD*"
#df = spark.read.csv("hdfs://localhost:9000/*")

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
      
df_binance = spark.read.format("csv") \
      .option("header", True) \
      .schema(schema) \
      .load(path)
df_binance.show(5)
print(df_binance.show(5))