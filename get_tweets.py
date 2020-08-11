import urllib.parse
#from twitter_api import api
from dotenv import api

if __name__ == "__main__":
#     results = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
#The index includes between 6-9 days of Tweets.

#Geolocalization: the search operator “near” isn’t available in the API, but there is a more precise way to restrict your query by a given location using the geocode parameter specified with the template “latitude,longitude,radius”, for example, “37.781157,-122.398720,1mi”. When conducting geo searches, the search API will first attempt to find Tweets which have lat/long within the queried geocode, and in case of not having success, it will attempt to find Tweets created by users whose profile location can be reverse geocoded into a lat/long within the queried geocode, meaning that is possible to receive Tweets which do not include lat/long information




    results = api.GetSearch(
        term="(police chokehold) OR (pepperspray) OR (rubber bullets) OR (tazed) OR (teargas) OR (police assualt) OR (mace) OR (police shooting) OR (police hitting) OR (police attack)",
        #geocode="-180,-90,180,90",
        since="2019-08-01",
        lang="en",
        count=100)
    for tweet in results:
        print(tweet)
    print(len(results))


#this git hub uses machine learning to predict citites of tweets
# https://github.com/shawn-terryah/Twitter_Geolocation
