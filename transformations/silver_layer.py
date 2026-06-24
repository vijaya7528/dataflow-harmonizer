from pyspark.sql import SparkSession

def silver_layer():

    spark = SparkSession.builder.getOrCreate()

    df = spark.read.parquet(
        "s3://dataflow-bronze-dev/customers/"
    )

    cleaned_df = (
        df
        .dropDuplicates()
        .na.fill("UNKNOWN")
    )

    cleaned_df.write \
        .mode("overwrite") \
        .parquet(
            "s3://dataflow-silver-dev/customers/"
        )

    return cleaned_df.count()
