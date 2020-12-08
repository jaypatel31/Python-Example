import json
import urllib.request, urllib.parse, urllib.error
import matplotlib.pyplot as plt
import numpy as np
fhand = urllib.request.urlopen('https://api.covid19india.org/data.json')
data = fhand.read()

jsdata = json.loads(data)
sr = jsdata["cases_time_series"]
total = len(jsdata["cases_time_series"])
total = int(total)
cnfirm =list()
recoverd = list()
decesed = list()
for elem in sr:
    cnfirm.append(int(elem["totalconfirmed"]))
    recoverd.append(int(elem['totalrecovered']))
    decesed.append(int(elem['totaldeceased']))

ypoints = np.array(cnfirm)
y2points = np.array(recoverd)
y3points = np.array(decesed)
plt.plot(ypoints,c="red",label='Total Confirmed')
plt.plot(y2points,c="green",label='Total Recovered')
plt.plot(y3points,c="magenta",label='Total Deceased')
plt.xlabel('Days')
plt.yticks(np.arange(0, 9703838))
plt.ylabel('Number of patient')
plt.title("Covid Cases")
plt.legend()
plt.show()
