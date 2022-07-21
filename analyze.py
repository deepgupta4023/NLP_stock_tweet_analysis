from socket import TCP_NODELAY
from transformers import MODEL_FOR_SEQUENCE_CLASSIFICATION_MAPPING, AutoModelForSequenceClassification, AutoTokenizer
from scipy.special import softmax
import numpy as np
import pandas as pd
import string

#load model and tokenizer

roberta="cardiffnlp/twitter-roberta-base-sentiment"
model=AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer=AutoTokenizer.from_pretrained(roberta)

labels=['Negative','Neutral','Positive']

#preprocessing
def preprocessing(tweet_str):
    tweet_words=[]
    for word in tweet_str.split(" "):
        if word.startswith("@") and len(word)>1:
            word="@user"
        elif word.startswith("http"):
            word="http" 

        tweet_words.append(word)
    processed_tweet=" ".join(tweet_words)
    return(processed_tweet)




#sentiment analysis
def tweet_analysis(processed_tweet):
    encoded_tweet= tokenizer(processed_tweet,return_tensors="pt")
    output= model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
    # or output= model(**encoded_tweet)  //does the same thing

    scores= output[0][0].detach().numpy()

    return(scores)





def analyze_tweets(df:pd.DataFrame):
    result={
        "Positive":0,
        "Neutral":0,
        "Negative":0
    }
    for i in range(len(df)):
        tweet=df.tweet[i]
        #print(tweet)
        processed_tweet= preprocessing(tweet)
        analysis= tweet_analysis(processed_tweet)
        if np.argmax(analysis)==0:
            result["Negative"]=result["Negative"]+1
        elif np.argmax(analysis)==1:
            result["Neutral"]=result["Neutral"]+1
        else:
            result["Positive"]=result["Positive"]+1
    print("tweet analyzed")
    return result