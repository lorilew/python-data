import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_327799.xml'

conn = urllib.urlopen(url)
xml = conn.read()

tree = ET.fromstring(xml)
comments = tree.findall("comments/comment")

print sum(int(comment.find("count").text) for comment in comments)
