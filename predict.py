from __future__ import print_function

import json
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

import boto3

# AWS Bucket Configuration
s3 = boto3.resource('s3')
sentiment_bucket = s3.Bucket("twitter.sentiment")


def handler(event, context):

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    body = s3.Object(bucket, key).get()["Body"].read()
    tweets = json.loads(body)

    # Load clf and vocabulary
    with open('models/clf.pkl', 'rb') as fmodel:
        clf = pickle.load(fmodel)
    with open('models/vocabulary.pkl', 'rb') as fvocabulary:
        vocabulary = pickle.load(fvocabulary)

    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.8,
                                 stop_words='english',
                                 use_idf=True, vocabulary=vocabulary)
    tweets_vectors = vectorizer.fit_transform(tweets)

    pred_multinomial = clf.predict(tweets_vectors)
    prob_multinomial = clf.predict_proba(tweets_vectors)

    sentiment_tweets = []
    for index, prob in enumerate(prob_multinomial):
        sentiment_tweets.append({"Tweet": tweets[index], "p_neg": prob[0],
                                 "p_pos": prob[1],
                                 "target": pred_multinomial[index]})
    dump = json.dumps(sentiment_tweets)

    file_name = 'sentiment_' + key
    sentiment_bucket.put_object(Body=dump, Key=file_name)
    return {"status": True}
