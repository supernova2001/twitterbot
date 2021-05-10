#bearer token:AAAAAAAAAAAAAAAAAAAAAL5tPQEAAAAAZ9edmrNtwMieNRhVLSzm%2BRpxExU%3D26UmMOcPjfMv6nfF1wRiA3Rk39uQZ3LGyqFGWDlBTufurF3t7Q
import tweepy
import time
consumer_key='vK1uAjfvtV8hNLhJlyQOyFe2K'
consumer_secret='G0C5a7D30sJHflYf4U9t9HdK0LgF20mLqCB7sznqLWKsUuUVHd'
key='1391012301939957761-gyjCuVtJHWVgiPVHZYdVLPevSja7Py'
secret='COlnB1NfY257ZALMydjeIIm0a3iRnK2dV0F57D9tK2EJj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

FILE_NAME='last_seen.txt'
api = tweepy.API(auth)
#api.update_status('No duplicate Tweets are allowed')
def read_last_seen(FILE_NAME):
    read_file=open(FILE_NAME,'r')
    last_seen_id=int(read_file.read().strip())
    read_file.close()
    return last_seen_id 

def store_last_seen(FILE_NAME,last_seen_id):
    file_write=open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return 

tweets=api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode='extended')
print(tweets)
def replyfunction():
    for tweet in reversed(tweets):
        try:
            api.update_status("@"+ tweet.user.screen_name+" Nakka Picchala Pulusu thinu ra Nakka ", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME,tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)
while(True):
    replyfunction()
