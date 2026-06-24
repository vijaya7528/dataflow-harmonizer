import boto3

glue = boto3.client("glue")

def start_crawler():

    glue.start_crawler(

        Name="customer_summary_crawler"

    )

    print(
        "Crawler execution started"
    )
