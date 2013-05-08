import sys
import re
import json

def main():
  tweet_file = open(sys.argv[1])

  tweets = loadTweets(tweet_file)

  wordDict = {}

  for tweet in tweets:
        addTweetWordsToDict(tweet, wordDict)

  numWords = len(wordDict.keys())
  for k in wordDict:
    print k, "{:4f}".format(float(wordDict[k])/float(numWords))

def loadTweets(fp):
  tweets = []
  for line in fp:
    tweet = json.loads(line)
    if u'text' in tweet:
      tweets.append(tweet[u'text'].encode('utf-8'))

  return tweets

def addTweetWordsToDict(tweet, wordDict):
  tweet_split = tweet.split()
  sent_sum = 0
  for tweet_word in tweet_split:
      wordDict[tweet_word] = wordDict.get(tweet_word,0) + 1

if __name__ == '__main__':
    main()
