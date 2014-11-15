from twython import Twython, TwythonError

APP_KEY = "GTobQXSpsCjzyMMtv1bDA"
APP_SECRET = "x8Ytf7yGuADTTideYOAVtZC8BXdF9RIp5rcuGmnPk"
OAUTH_TOKEN = "17181709-vf5UQI8M7eyjdoRMLzDXBR4SUdb4LZEPHQMqA0dSp"
OAUTH_TOKEN_SECRET = "YU6faELiBNn92vK1PSqzvpAAJUbbgFQemJUKB1m98"

# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
    search_results = twitter.search(q='#weather #hamont', count=10)
except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n'
