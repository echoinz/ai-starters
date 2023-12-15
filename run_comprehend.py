import boto3
# Currently works with only for documents
session = boto3.Session(profile_name='ai_starters')

client = session.client('comprehend')
# Run pii_entities_detection_job
response = client.start_pii_entities_detection_job(
    InputDataConfig={
        'S3Uri': 's3://ai-starters/aws-comprehed-analytics-incoming/pii_sample_data',
        'InputFormat': 'ONE_DOC_PER_FILE'
    },
    OutputDataConfig={
        'S3Uri': 's3://ai-starters/aws-comprehed-analytics-outcoming/sample-data-api'
    },
    Mode='ONLY_REDACTION',
    RedactionConfig={
        'PiiEntityTypes': [
            'BANK_ACCOUNT_NUMBER','BANK_ROUTING','CREDIT_DEBIT_NUMBER','CREDIT_DEBIT_CVV','CREDIT_DEBIT_EXPIRY','PIN','EMAIL','ADDRESS','NAME','PHONE','SSN','DATE_TIME','PASSPORT_NUMBER','DRIVER_ID','URL','AGE','USERNAME','PASSWORD','AWS_ACCESS_KEY','AWS_SECRET_KEY','IP_ADDRESS','MAC_ADDRESS','ALL','LICENSE_PLATE','VEHICLE_IDENTIFICATION_NUMBER','UK_NATIONAL_INSURANCE_NUMBER','CA_SOCIAL_INSURANCE_NUMBER','US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER','UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER','IN_PERMANENT_ACCOUNT_NUMBER','IN_NREGA','INTERNATIONAL_BANK_ACCOUNT_NUMBER','SWIFT_CODE','UK_NATIONAL_HEALTH_SERVICE_NUMBER','CA_HEALTH_NUMBER','IN_AADHAAR','IN_VOTER_NUMBER',
        ],
        'MaskMode': 'REPLACE_WITH_PII_ENTITY_TYPE'
    },
    DataAccessRoleArn='arn:aws:iam::703790562860:role/service-role/AmazonComprehendServiceRoleS3FullAccess-ai_starters_s3_access',
    JobName='string',
    LanguageCode='en',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)
print(response)

