# pip install snscrape

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(bangalore OR bengaluru) (flood OR floods OR flooded OR bangalorefloods OR bengalurufloods OR heavyrain OR rain OR rains) (help OR relief OR shelter OR food OR rescue) until:2017-10-01 since:2017-07-01"

tweets = []
limit = 5000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        # print(type(tweet))
        tweets.append([tweet.date, tweet.user.username, tweet.rawContent])
        # tweets.append(tweet.rawContent)
        # print(tweet.coordinates)
    
# print(tweets)
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
df

# to save to csv
# df.to_csv('tweets.csv')
