import requests
import pprint
import pandas as pd
import csv

month = "06"

'''
108 서울 114 원주 133 대전 146 전주 156 광주 159 부산 184 제주 143 대구
'''
region = [108, 114, 133, 146, 156, 159, 184, 143]
'''
avgTa = 평균 기온  avgWs = 평균 풍속  avgRhm = 평균 상대습도  stnNm = 지명
'''
result = ['avgTa', 'avgWs', 'avgRhm']
average = [0, 0, 0]

f = open('test_file.csv', 'w', newline='')
wr = csv.writer(f)

for i in region:
    sample_list = []
    avg = 0
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey=jCAu%2By2rHxF3JN9k%2BXwhS%2FRDwWIRS9O3ln2p%2Fdxx%2BRNj3deacKcMXUQv9Cn5EJSJet3sBrb41dp%2BJLK%2FNpfk%2Bw%3D%3D&numOfRows=10&pageNo=1&dataType=JSON&dataCd=ASOS&dateCd=DAY&startDt=20200610&endDt=20200620&stnIds="+str(i)
    response = requests.get(url)
    responseJson = response.json()
    for j in range(10):
        average[0] = average[0] + float(responseJson['response']['body']['items']['item'][j]['avgTa'])
        average[1] = average[1] + float(responseJson['response']['body']['items']['item'][j]['avgWs'])
        average[2] = average[2] + float(responseJson['response']['body']['items']['item'][j]['avgRhm'])
    for k in range(3):
        average[k] = average[k] / 10
    sample_list.append(responseJson['response']['body']['items']['item'][0]['stnNm'])
    sample_list.append(str(round(average[0], 2)))
    sample_list.append(str(round(average[1], 2)))
    sample_list.append(str(round(average[2], 2)))
    wr.writerow(sample_list)

f.close()
