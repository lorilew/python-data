import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
url = serviceurl + urllib.urlencode({'sensor':'false', 'address':'Elon University'})

conn = urllib.urlopen(url)
data = conn.read()

js = json.loads(data)

print json.dumps(js['results'][0]['place_id'], indent=4, sort_keys=True)
