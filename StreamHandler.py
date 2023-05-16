from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("Stream Handler").master("local[*]").getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "s-fog").option("startingOffsets", "latest").load()

    df.printSchema()

    df = df.selectExpr("CAST(value AS STRING)")

    schema = StructType([
        StructField("SensorId", IntegerType()),
        StructField("HomeId", IntegerType()),
        StructField("Timestamp", DoubleType()),
        StructField("Volume", DoubleType()),
        StructField("Velocity", DoubleType()),
        StructField("Pressure", DoubleType()),
        StructField("pH", DoubleType()),
        StructField("Temperature", DoubleType()),
        StructField("Turbidity", DoubleType()),
        StructField("Pollution level", DoubleType())
    ])

    df = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

    df.printSchema()

    # stream_df_new = stream_df.select(\
    #             from_json(stream_df.value.cast("string"),\
    #             StructType().add("Date", StringType())\
    #                         .add("Price", DoubleType())).alias("INFO")\
    #             ,"key", "timestamp"
    #             ).select("INFO.*")
    
    # orders_agg_write_stream = stream_df_new \
    #     .writeStream \
    #     .format('console') \
    #     .trigger(processingTime='5 seconds') \
    #     .start()
    

    df = df.withColumn("Timestamp", to_timestamp(col("Timestamp")))

    # df = df.withWatermark("Timestamp", "10 seconds")

    # query = df.groupBy("HomeId").agg(collect_list("Timestamp").alias("Timestamps")) \
    #     .writeStream \
    #     .outputMode("update") \
    #     .format("console") \
    #     .start()

    query = df.writeStream.format("console").trigger(processingTime= '5 seconds').start()

    query.awaitTermination()

if __name__ == "__main__":
    main()
