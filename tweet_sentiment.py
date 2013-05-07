import sys
import re
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiments = loadSentiment(sent_file)
    tweets = loadTweets(tweet_file)

    for tweet in tweets:
      print calculateSentiment(tweet, sentiments)

def loadSentiment(fp):
  sent = {}

  for line in fp:
    line_split = re.split(r'(\t+)',line)
    sent[line_split[0]] = int(line_split[2])

  return sent

def loadTweets(fp):
  tweets = []
  for line in fp:
    tweet = json.loads(line)
    if u'text' in tweet:
      tweets.append(tweet[u'text'])

  return tweets

def calculateSentiment(tweet, sentiments):
  tweet_split = re.split(r'(\s+)',tweet)
  sent_sum = 0
  for tweet_word in tweet_split:
    if tweet_word in sentiments:
      sent_sum += sent_sum + int(sentiments[tweet_word])
  return sent_sum

if __name__ == '__main__':
    main()
