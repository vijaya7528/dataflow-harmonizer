# dataflow-harmonizer
Built an AWS-based metadata discovery framework that automated Glue Crawler creation, daily catalog refresh, and cross-account S3 data movement, reducing manual effort by 95% and enabling seamless Athena-based analytics.

## Overview

DataFlow Harmonizer is a cloud-native data engineering framework built on AWS.

The project ingests raw data into Amazon S3, performs transformations using PySpark on EMR Serverless, distributes curated datasets across AWS accounts, automatically refreshes metadata using AWS Glue Crawlers, and enables querying through Amazon Athena.

## Features

- Data Lake Architecture (Raw, Bronze, Silver, Gold)
- PySpark Transformations
- EMR Serverless Processing
- Multithreaded S3 Data Transfers
- AWS Glue Crawler Automation
- Athena Integration
- Audit Framework
- Logging Framework

## AWS Services Used

- Amazon S3
- AWS Glue
- AWS Athena
- Amazon EMR Serverless
- Amazon RDS
- IAM
- CloudWatch

## Architecture

Source Systems
→ S3 Raw
→ PySpark
→ Bronze
→ Silver
→ Gold
→ Glue Catalog
→ Athena
→ RDS
