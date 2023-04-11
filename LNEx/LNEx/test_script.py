import json, re
from shapely.geometry import MultiPoint

import sys 
sys.path.append("LNEx")
import LNEx as lnex

def read_tweets():
    tweets_file = "_Data/sample_tweets.txt"
    # read tweets from file to list
    with open(tweets_file) as f:
        tweets = f.read().splitlines()
    return tweets

def init_using_elasticindex(bb, cache, augmentType, dataset, capital_word_shape):
    lnex.elasticindex(conn_string='localhost:9200', index_name="photon")

    geo_info = lnex.initialize( bb, augmentType=augmentType,
                                    cache=cache,
                                    dataset_name=dataset,
                                    capital_word_shape=capital_word_shape)
    return geo_info

bbs = { "chennai": [12.74, 80.066986084, 13.2823848224, 80.3464508057],
        "louisiana": [29.4563, -93.3453, 31.4521, -89.5276],
        "houston": [29.4778611958, -95.975189209, 30.1463147381, -94.8889160156],
        "banglore": [12.5, 75, 15, 80]}



dataset = "banglore"

geo_info = init_using_elasticindex(bbs[dataset], cache=True, augmentType="HP", 
                                   dataset=dataset, capital_word_shape=False)

# print(geo_info)
with open("C://Users//20UCS005//Desktop//BTP//LNEx//_Data//Cached_Gazetteers//banglore_geo_info.json") as f:
    geo_information = json.load(f)

# with open(".\_Data\chennai_extended_words3.json") as f:
#     words3 = json.load(f)
# print(geo_information["1"]["geo_item"]["point"]["lat"],geo_information["1"]["geo_item"]["point"]["lon"])
# lnex.initialize_using_files(geo_locations, words3)
file = open("C://Users//20UCS005//Desktop//BTP//LNEx//_Data//coordinates.txt","a")
for tweet in read_tweets():
    for output in lnex.extract(tweet):
        id_l = output[3]["main"]
        if len(id_l) != 0:
            # print(geo_information[id_l[0]]["geo_item"]["point"]["lat"],geo_information[id_l[0]]["geo_item"]["point"]["lon"])
            file.writelines([str(geo_information[id_l[0]]["geo_item"]["point"]["lat"])+" ",str(geo_information[id_l[0]]["geo_item"]["point"]["lon"])+"\n"])
        print(output[0],output[1],output[2],output[3]['main'])
    print("#"*50)

file.close()
