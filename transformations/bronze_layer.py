from pyspark.sql import SparkSession

def bronze_layer():

    spark = SparkSession.builder \
        .appName("Bronze Layer") \
        .getOrCreate()

    customer_df = spark.read \
        .option("header", True) \
        .csv("s3://dataflow-raw-dev/customers/")

    customer_df.write \
        .mode("overwrite") \
        .parquet(
            "s3://dataflow-bronze-dev/customers/"
        )

    return customer_df.count()
