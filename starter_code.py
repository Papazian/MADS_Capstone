import boto3
import pandas as pd

# Downloaded the data from here
# https://www.consumerfinance.gov/data-research/consumer-complaints/#get-the-data

s3 = boto3.client('s3')
obj = s3.get_object(Bucket='aletheia-public', Key='complaints_16Jun2026_sampled.csv')
df = pd.read_csv(obj['Body'])

df.head()