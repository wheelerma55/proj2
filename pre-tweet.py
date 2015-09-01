#import regex
import re

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#Read the tweets one by one and process it
fp = open('outmod.txt', 'r')
#fp = open('data/sampleTweets.txt', 'r')
line = fp.readline()
outline = open('pt-outmode.txt', 'w')
while line:
    processedTweet = processTweet(line)
    outline.write(processedTweet)
#    print processedTweet
    line = fp.readline()
#end loop
fp.close()
outline.close()

