# The program will prompt for a URL,
# read the JSON data from that URL using urllib and then parse
# and extract the comment counts from the JSON data, compute the
# sum of the numbers in the file and enter the sum below:

import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_327803.json'

conn = urllib.urlopen(url)
data = conn.read()

js = json.loads(data)

print sum(int(comment['count']) for comment in js['comments'])
