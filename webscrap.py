import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
countnm = input('Enter The Count - ')
position = input('Enter THe Position')

def call(idurl):
    html = urllib.request.urlopen(idurl).read()
    soup = BeautifulSoup(html,'html.parser')
    global tags
    tags = soup('a')

call(url)
countnm= int(countnm)
position = int(position)-1
i=0

while i < countnm:
    newurl = tags[position].get('href',None)
    print(newurl)
    i=i+1
    call(newurl)
