import urllib
import json

for i in range(10):
	url = "http://search.twitter.com/search.json?q=microsoft&page="+str(i+1)
	response = urllib.urlopen(url)
	dict = json.load(response)
	tweets = dict['results']

	for tweet in tweets:
		print tweet[u'text'].encode('utf-8')
