import sys
import re
import json

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  sentiments = loadSentiment(sent_file)
  output = {}
  tweets = loadTweets(tweet_file)

  for tweet in tweets:
    calculateSentiment(tweet, sentiments, output)

  for tweet_word in output:
    print tweet_word, output[tweet_word].getSent()

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
      tweets.append(tweet[u'text'].encode('utf-8'))

  return tweets

def calculateSentiment(tweet, sentiments, output):
  tweet_split = tweet.split()
  sent_sum = float(0)
  for tweet_word in tweet_split:
    if tweet_word in sentiments:
      sent_sum += sent_sum + float(sentiments[tweet_word])

  for tweet_word in tweet_split:
    if tweet_word in output:
      term = output[tweet_word]
    else:
      term = Term(tweet_word)
      output[tweet_word] = term

    if tweet_word in sentiments:
      term.addSent(float(sentiments[tweet_word]))
    else:
      term.addSent(float(sent_sum))



class Term:
  def __init__(self, term):
    self.term = term
    self.sent = float(0)

  def getTerm(self):
    return self.term

  def getSent(self):
    return float(self.sent)

  def addSent(self, sent):
      self.sent += float(sent)

if __name__ == '__main__':
    main()
