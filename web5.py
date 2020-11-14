import urllib.request, urllib.parse, urllib.error
import json
url = input('Enter - ')
fhand = urllib.request.urlopen(url)
data = fhand.read()
print('Retrieved', len(data), 'characters')


info = json.loads(data)
itr = info['comments']
sum = 0
for single in itr:
    sum = sum + int(single['count'])

print(sum)
