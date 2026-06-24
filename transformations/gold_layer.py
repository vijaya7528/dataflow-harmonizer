from pyspark.sql import SparkSession
from pyspark.sql.functions import count

def gold_layer():

    spark = SparkSession.builder.getOrCreate()

    customer_df = spark.read.parquet(
        "s3://dataflow-silver-dev/customers/"
    )

    city_summary = customer_df.groupBy(
        "city"
    ).agg(
        count("*").alias(
            "customer_count"
        )
    )

    city_summary.write \
        .mode("overwrite") \
        .parquet(
            "s3://dataflow-gold-dev/customer_summary/"
        )

    return city_summary.count()
