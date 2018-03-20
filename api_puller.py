import requests
from objdict import ObjDict

url = "******"

headers = {'accessToken': '*******'}

x = 192
count = x/20

res = x%20

if res!=0:
    count = count+1

total_results = ''
total_count = 0

for i in range(0, count):

    querystring = {"url":"https%3A%2F%2Ftracxn.com%2Ftheme%2Fmyfeeds%2Ffeedview%23%257CpracticeArea%253DTechnology%257CtotalMoneyRaised%255Emin%253D0%255Emax%253D4000000%257Csort%253DeditorRating%257Corder%253DDEFAULT","from":total_count}
    response = requests.request("GET", url, headers=headers, params=querystring)
    total_count = total_count+20
    total_results = total_results+response.text

print total_results

f = open('out.txt', 'w')
f.write(total_results)
f.close()
