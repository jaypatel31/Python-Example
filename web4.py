import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')
fhand = urllib.request.urlopen(url)
data = fhand.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum=0
for num in counts:
    sum = sum + int(num.text)

print(sum)
