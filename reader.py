import json
import uuid
from datetime import datetime

import boto3
import tweepy
from tweepy import OAuthHandler

consumer_key = 'yourkey'
consumer_secret = 'yourkey'
access_token = 'yourkey'
access_secret = 'yourkey'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

search_text = "trump"
limit = 50
lang = ["en"]

# AWS Bucket Configuration
s3 = boto3.resource('s3')
bucket_name = "twitter.reader"
bucket = s3.Bucket(bucket_name)

def generate_random_filename():
    uuid_file = str(uuid.uuid4())[:10]
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    return "{}_{}.csv".format(uuid_file, date)

def handler(event, context):
    file_name = generate_random_filename()

    tweets = []
    for tweet in tweepy.Cursor(api.search, q='trump', languages=["en"]).items(50):
        tweets.append(tweet.text)
    dump = json.dumps(tweets)

    bucket.put_object(Body=dump, Key=file_name)
    return {"status": True}
