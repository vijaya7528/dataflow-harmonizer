from datetime import datetime

def audit_record(
        pipeline_name,
        source_count,
        target_count,
        status,
        error_message=None):

    audit_data = {

        "pipeline_name": pipeline_name,

        "start_time": datetime.now(),

        "source_count": source_count,

        "target_count": target_count,

        "status": status,

        "error_message": error_message

    }

    print(audit_data)
