import api
import search
import analyze
import pandas as pd


top_stocks=pd.read_csv('nse_gainers.csv')
bottom_stocks=pd.read_csv('nse_losers.csv')


connected_api=api.connect()
def function(keyword):
    tweets= search.search_tweets(api= connected_api, keyword=keyword)
    #print(tweets)
    results=analyze.analyze_tweets(tweets)
    print(results)

for i in range(len(top_stocks.SYMBOL)):
    function(keyword=top_stocks.SYMBOL[i])


for i in range(len(bottom_stocks.SYMBOL)):
    function(keyword=bottom_stocks.SYMBOL[i])

#print(keyword)