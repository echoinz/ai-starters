import boto3
import run_comprehend

# Currently works with only for documents
session = boto3.Session(profile_name='ai_starters')
client = session.client('comprehend')
pii_comprehendWrapper = run_comprehend.ComprehendWrapper(client, 's3://ai-starters/aws-comprehed-analytics-incoming/pii_sample_data',
                  's3://ai-starters/aws-comprehed-analytics-outcoming/pii_sample_data',
                  'arn:aws:iam::703790562860:role/service-role/AmazonComprehendServiceRoleS3FullAccess-ai_starters_s3_access')


pii_comprehendWrapper.run_pii_entities_detection_job()

sa_comprehendWrapper = run_comprehend.ComprehendWrapper(client, 's3://ai-starters/aws-comprehed-analytics-incoming/sentiment_sample_data',
                  's3://ai-starters/aws-comprehed-analytics-outcoming/sentiment_sample_data',
                  'arn:aws:iam::703790562860:role/service-role/AmazonComprehendServiceRoleS3FullAccess-ai_starters_s3_access')


sa_comprehendWrapper.run_sentiment_detection_job()
