import requests
import pprint
import pandas as pd

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey=jCAu%2By2rHxF3JN9k%2BXwhS%2FRDwWIRS9O3ln2p%2Fdxx%2BRNj3deacKcMXUQv9Cn5EJSJet3sBrb41dp%2BJLK%2FNpfk%2Bw%3D%3D&numOfRows=10&pageNo=1&dataType=JSON&dataCd=ASOS&dateCd=DAY&startDt=20100101&endDt=20100102&stnIds=108"

response = requests.get(url)
responseJson = response.json()


df = pd.json_normalize(responseJson['response'])
pprint.pprint(responseJson)
print(df)
