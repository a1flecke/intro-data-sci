import sys
import re
import json

def main():
  tweet_file = open(sys.argv[1])

  tweet_entites = loadTweets(tweet_file)
  hash_tags= {}
  hash_tag_objs = []

  for tweet in tweet_entites:
     addHashTags(hash_tags, tweet)

  buildHashTagObjs(hash_tag_objs, hash_tags)

  #sorted(state_objs, key=StateObj.getSent).pop()

  hash_tag_objs = sorted(hash_tag_objs, key=HashTag.getCount)

  top_ten = []
  for index in range(1,11):
    top_ten.append(hash_tag_objs.pop())

  for index in range(0,10):
    print top_ten[index].getTag(), float(top_ten[index].getCount())

def buildHashTagObjs(hash_tag_objs, hash_tags):
  for k in hash_tags:
    hash_tag_objs.append(HashTag(k, hash_tags[k]))

def loadTweets(fp):
  tweets = []
  for line in fp:
    tweet = json.loads(line)
    if u'entities' in tweet:
      entities = tweet[u'entities']
      if u'hashtags' in entities:
        tweets.append(tweet[u'entities'])
      else:
        print 'Tweet did not have any hash tags'

  return tweets

def addHashTags(hash_tags, tweet):
  tags = getHashTagsForTweet(tweet)

  for tag in tags:
    tag_text = tag[u'text'].encode('utf-8')
    hash_tags[tag_text] = hash_tags.get(tag_text, 0) + 1
    #state_sents[tweet.getState()] = state_sents.get(tweet.getState(), 0) + 1

def getHashTagsForTweet(tweet):
  if u'hashtags' in tweet:
    return tweet[u'hashtags']
  else:
    return []

class HashTag:
  def __init__(self, tag, count):
    self.tag = tag
    self.count = count

  def getTag(self):
    return self.tag

  def getCount(self):
    return self.count

if __name__ == '__main__':
    main()
