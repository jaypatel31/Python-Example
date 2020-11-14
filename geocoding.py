import urllib.request, urllib.parse, urllib.error
import json

url='http://py4e-data.dr-chuck.net/json?'
apikey = 42
while True:
    addr = input('Enter Address - ')
    if len(addr)< 1:
        break
    parms = dict()
    parms['address'] = addr
    parms['key'] = apikey
    mainurl = url+urllib.parse.urlencode(parms)

    print('Retrieving......',mainurl)
    uh = urllib.request.urlopen(mainurl)
    data =uh.read().decode()
    print('Retrived:',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js=None

    if not js or 'Status' in js or js['status'] != 'OK':
        print("Failed To Retrive")
        print(data)
        continue
    print('place_id:',js['results'][0]['place_id'])
