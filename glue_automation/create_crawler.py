import boto3

glue = boto3.client("glue")

def create_crawler():

    glue.create_crawler(

        Name="customer_summary_crawler",

        Role="AWSGlueServiceRole",

        DatabaseName="sales_db",

        Targets={

            "S3Targets": [

                {
                    "Path":
                    "s3://dataflow-gold-dev/customer_summary/"
                }

            ]
        }
    )
