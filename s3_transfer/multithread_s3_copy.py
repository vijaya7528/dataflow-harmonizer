import boto3
import threading

s3 = boto3.client("s3")

def copy_dataset(source_bucket,
                 target_bucket,
                 object_key):

    copy_source = {

        'Bucket': source_bucket,
        'Key': object_key

    }

    s3.copy_object(

        CopySource=copy_source,

        Bucket=target_bucket,

        Key=object_key

    )

    print(f"{object_key} copied")

def execute_parallel_copy():

    files = [

        "customers/customer.parquet",

        "orders/orders.parquet",

        "products/products.parquet"

    ]

    threads = []

    for file in files:

        thread = threading.Thread(

            target=copy_dataset,

            args=(
                "dataflow-gold-dev",
                "reporting-bucket",
                file
            )
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()
