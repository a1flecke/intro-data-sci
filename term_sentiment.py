import sys
import re
import json

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  sentiments = loadSentiment(sent_file)
  tweets = loadTweets(tweet_file)

  for tweet in tweets:
    calculateSentiment(tweet, sentiments)

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
  tweet_split = tweet.split()
  sent_sum = 0
  for tweet_word in tweet_split:
    if tweet_word in sentiments:
      sent_sum += sent_sum + int(sentiments[tweet_word])

  for tweet_word in tweet_split:
    if tweet_word in sentiments:
      print tweet_word, int(sentiments[tweet_word])
    else:
      print tweet_word, sent_sum

if __name__ == '__main__':
    main()
