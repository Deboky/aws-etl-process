# Writing ETL Job In Lambda and Cleaning Data

import awswrangler as wr
import pandas as pd
import urllib.parse
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']

def lambda_handler(event, context):
    # Log the start of the Lambda function
    logger.info('Lambda function has started')
    
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        # Log the S3 bucket and object key being processed
        logger.info(f'Processing file {key} from bucket {bucket}')
        
        # Creating DF from content
        df_raw = wr.s3.read_json(f's3://{bucket}/{key}')

        # Extract required columns:
        df_step_1 = pd.json_normalize(df_raw['items'])

        # Log the shape of the dataframe
        logger.info(f'Dataframe shape: {df_step_1.shape}')
        
        # Write to S3
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation
        )

        # Log the success of the write operation
        logger.info('Data written successfully to S3')
        
        return wr_response
    except Exception as e:
        # Log the exception
        logger.error(f'Error processing object {key} from bucket {bucket}', exc_info=True)
        raise e
