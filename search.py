import tweepy
import pandas as pd
import string

def search_tweets(api, keyword='nse', limit=300):
    data= []
    columns= ['tweet']
   
    print("New keyword is:", keyword)
    
    tweets = tweepy.Cursor(api.search_tweets, q='#'+keyword, count=200, tweet_mode='extended').items(limit)
    print("search started")
    for tweet in tweets:
        data.append([tweet.full_text])
    
    df = pd.DataFrame(data, columns=columns, index=None)
    
    print("tweets searched and returned")
    return df
    