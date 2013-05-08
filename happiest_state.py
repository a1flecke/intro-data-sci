import sys
import re
import json

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  sentiments = loadSentiment(sent_file)
  tweets = loadTweets(tweet_file)
  state_sents = {}

  states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

  sentiments = loadSentiment(sent_file)
  tweets = loadTweets(tweet_file)

  for tweet in tweets:
     addToStateSent(state_sents, tweet, calculateSentiment(tweet, sentiments))

  state_objs = buildStateObjs(state_sents)
  happiest = state_objs.sorted(key=StateObj.getSent).pop()
  print happiest.getName(), happiest.getSent()

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
      state = getStateForTweet(tweet)

      if state != "":
        tweets.append(Tweet(tweet[u'text'], state))

  return tweets

def calculateSentiment(tweet, sentiments):
  tweet_split = re.split(r'(\s+)',tweet.getText())
  sent_sum = 0
  for tweet_word in tweet_split:
    if tweet_word in sentiments:
      sent_sum += sent_sum + int(sentiments[tweet_word])
  return sent_sum

def getStateForTweet(tweet):
  if u'user' in tweet:
    print tweet[u'user']
    user = json.loads(tweet[u'user'])
    if u'lang' in user and user[u'lang'] == 'en':
      if u'location' in user:
        location = user[u'location']
        match = re.match(',\s+(AL|AK|AZ|AR|CA|CO|CT|DC|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY)')
        if match:
            return match.group(1)
  return ''

def addToStateSent(state_sents, tweet, sentiment):
  state_sents = state_sents.get(tweet.getState(), 0) + 1

def buildStateObjs(state_sents):
  state_objs = []
  for k in state_sents:
    state_objs.append(StateObj(k, state_sents[k]))

  return state_objs

class Tweet:
  def __init__(self, text, state):
    self.text = text
    self.state = state

  def getText():
    return self.text

  def getState():
    return self.state

class StateObj:

  def __init__(self, name, sent):
    self.name = name
    self.sent = sent

  def getName():
    return self.name

  def getSent():
    return self.sent

if __name__ == '__main__':
    main()
