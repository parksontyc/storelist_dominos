#-*- coding:utf-8 -*-
#!/usr/bin/env python
import requests
import json
import csv

store_code = []
store_name = []
store_address = []
store_tel = []
store_lat = []
store_lng = []

url = "https://www.dominos.com.tw/vConfig.htm"

form = {
	'c': 'gpMarker', 
	'f': '2||||||'
	}

res = requests.post(url, data=form, timeout=5)
data = json.loads(res.content)

for row in data:
#     print row
    store_code.append(row['code'])
    store_name.append(row['name'])
    store_address.append(row['addr'])
    store_tel.append(row['tel'])
    store_lat.append(row['lat'])
    store_lng.append(row['lng'])
    
    #print (store_code)

with open('shop_list_dominos.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市代號', '門市名稱', '門市地址', '門市電話', '門市lat座標', '門市lng座標']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_code)):
        newrow.clear()
        newrow.append(store_code[n])
        newrow.append(store_name[n])
        newrow.append(store_address[n])
        newrow.append(store_tel[n])
        newrow.append(store_lat[n])
        newrow.append(store_lng[n])
        csvwriter.writerow(newrow)