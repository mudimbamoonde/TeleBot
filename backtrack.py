import requests
import json

re_api = requests.get("https://api.covid19api.com/dayone/country/Zambia")
# convert to JSON
results = re_api.json()
# loader = json.dumps(results)
# view = json.load(loader)
num = len(results)
confirmedCases = 0
active = 0
recovered = 0
death = 0
date_c = 0

for n in range(num):
    confirmedCases = results[n]["Confirmed"]
    active = results[n]["Active"]
    death = results[n]["Deaths"]
    recovered = results[n]["Recovered"]
    date_c = results[n]["Date"]

print("\n Date: {} \n Confirmed Case:{} \n Active Cases: {} \n Recoveries: {} \n Death: {}"
      .format(date_c, confirmedCases, active, recovered, death), end=" ")
