import json
import boto3
from boto3 import resource


def write_file_to_s3(bucket_name,file_name, file_content):
    s3 = resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.put_object(Key=file_name, Body=file_content )
    return 1
    
def read_file_from_s3(bucket_name,file_name):
    s3 = resource('s3')
    obj = s3.Object( bucket_name , file_name )
    file_content = obj.get()['Body'].read().decode('UTF-8')
    return file_content

def lambda_handler(event, context):
    
    # Initialize
    bucket_name = "your-bucket"
    file_name = "your folder/your file name"
    file_contents = "Momento Mori, Live each day like its your last!"
    
    # Write file to S3
    write_file_to_s3(bucket_name,file_name,file_contents)
    print("FILE CONTENTS WRITTEN TO S3: " + file_contents)
    
    # Read file from S3
    resultant_file_contents = read_file_from_s3(bucket_name,file_name)
    print("FILE CONTENTS READ FROM S3: " + resultant_file_contents)
    
    # Return success message
    return {
        'statusCode': 200,
        'body': json.dumps('Successful write to and read from S3')
    }
