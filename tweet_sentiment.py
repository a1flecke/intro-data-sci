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

    #for tweet in tweets:
     ##print tweet_sentiment

def loadSentiment(fp):
  sent = {}

  for line in fp:
    line_split = re.split(r'(\s+)',line)
    sent[line_split[0]] = line_split[2]

  return sent

def loadTweets(fp):
  for line in fp:
    tweet = json.loads(line)
    if u'text' in tweet:
      print tweet[u'text'].encode('utf-8')


if __name__ == '__main__':
    main()
