import json
import urllib.request, urllib.parse, urllib.error

print()
print("++++++++++++++++++Covid Cases Counter+++++++++++++++++++")
print()
print('......Loding')
fhand = urllib.request.urlopen('https://api.covid19india.org/data.json')
data = fhand.read()

jsdata = json.loads(data)
total = len(jsdata["cases_time_series"])
total = int(total)
todaydata = jsdata["cases_time_series"][total-1]
print()
print()
print("============= Today's Stats ==============")
print()
print("Today's New Cases : "+todaydata['dailyconfirmed'])
print()
print("Today's Death : "+ todaydata['dailydeceased'])
print()
print("Today's Recovered : "+todaydata['dailyrecovered'])
print()
print()
print("============= Total Stats ==============")
print()
print()
print("Total Confirmed Cases : "+todaydata['totalconfirmed'])
print()
print("Total Death : "+todaydata['totaldeceased'])
print()
print("Total Recovered : "+todaydata['totalrecovered'])
print()
print()
state = input("Enter Your State Full Name - ")
state = str.capitalize(state)
statese = jsdata['statewise']
found = 0
num = 0
for pt in statese:
    num += 1
    if pt['state'] == state:
        found = 1
        break;

if found ==1:
    print()
    print()
    print("~~~~~~~~~~~~~ "+state+" Stats ~~~~~~~~~~~~~~")
    print()
    print("Total Cases : "+jsdata['statewise'][num]['confirmed'])
    print()
    print("Total Death : "+ jsdata['statewise'][num]['deaths'])
    print()
    print("Total Recovered : "+jsdata['statewise'][num]['recovered'])
    print()
    print("Total Active : "+jsdata['statewise'][num]['active'])

