from transformations.bronze_layer import bronze_layer
from transformations.silver_layer import silver_layer
from transformations.gold_layer import gold_layer

from glue_automation.start_crawler import start_crawler

from s3_transfer.multithread_s3_copy import (
    execute_parallel_copy
)

from audit.audit import audit_record

from logging_framework.logger import logger


def run_pipeline():

    try:

        logger.info(
            "Pipeline Started"
        )

        bronze_count = bronze_layer()

        silver_count = silver_layer()

        gold_count = gold_layer()

        execute_parallel_copy()

        start_crawler()

        audit_record(

            pipeline_name="CustomerPipeline",

            source_count=bronze_count,

            target_count=gold_count,

            status="SUCCESS"
        )

        logger.info(
            "Pipeline Completed"
        )

    except Exception as e:

        logger.error(str(e))

        audit_record(

            pipeline_name="CustomerPipeline",

            source_count=0,

            target_count=0,

            status="FAILED",

            error_message=str(e)
        )


if __name__ == "__main__":

    run_pipeline()
