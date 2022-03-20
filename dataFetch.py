import os
# import config
import requests

# We make a dictionary headers to authenticate while performing GET request
headers = dict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer "+os.getenv("BEARER_TOKEN")

#This block of code fetches user details so we can get the id of user here to pass into the next block that fetches the recent tweets
def usernameToId(handle):
    userNameToidURL = f"https://api.twitter.com/2/users/by/username/{handle}"
    r = requests.get(url = userNameToidURL, headers = headers)
    data = r.json()
    userId = data["data"]['id']
    return userId

#This function gets the number of likes and retweets the given tweet(through ID) has
def getTweetEngagements(id):
    tweetUrl = f"https://api.twitter.com/2/tweets/{id}?tweet.fields=public_metrics"
    r = requests.get(url = tweetUrl, headers = headers)
    data = r.json()
    returnedList = []
    returnedList.append(data['data']['public_metrics']['like_count'])
    returnedList.append(data['data']['public_metrics']['retweet_count'])
    return returnedList

#This block of code gets the latest tweets whose likes and retweets are then fetched and returned
def fetchLatestTweets(username):
    userId = usernameToId(username)
    latestTweetsUrl = f"https://api.twitter.com/2/users/{userId}/tweets?max_results=20&exclude=replies,retweets"
    r=requests.get(url = latestTweetsUrl, headers = headers)
    data = r.json()
    tweetNos = [x for x in range(20,0,-1)]
    likes = []
    retweets = []
    testArr=[]
    print(type(data))
    for ele in data['data']:
        tweetId = ele['id']
        # testArr.append(tweetId)
        likes.append(getTweetEngagements(tweetId)[0])
        retweets.append(getTweetEngagements(tweetId)[1])
    # We reverse the lists returned as the latest tweet gets plotted first if not reversed
    # testArr.reverse()
    tweetNos.reverse()
    likes.reverse()
    retweets.reverse()
    return [tweetNos,likes,retweets]  

def finalReturn(username):
    return fetchLatestTweets(username)



    