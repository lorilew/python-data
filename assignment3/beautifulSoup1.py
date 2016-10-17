import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_327802.html"

html = urllib.urlopen(url).read() #String
soup = BeautifulSoup(html) #Soup = parsed html object

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup("span")
count = 0

for tag in tags:
  count = count + int(re.findall("[0-9]+", tag.string)[0])

print count
