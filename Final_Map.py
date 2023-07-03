from textwrap import fill
from turtle import color
import folium as fl
import webbrowser
import json
import pandas as pd

# 초기 위도 경도
lat = 36.321655
lng = 127.378953

# 행정구역 데이터 로드
geo = json.load(open('./Deajeon.geojson',encoding='utf-8'))

# 지도 객체 선언
m = fl.Map(location=[lat,lng],
        zoom_start=12,
        width=1000,
         height=800            
         )

# 지도 택시 하차수에 따른 행정구역 타일 색깔 구분
df = pd.read_csv('./taxi_off.csv')
df.head()
fl.Choropleth(
    geo_data=geo,
    data=df,
    columns=('동', '값'),
    key_on='feature.properties.temp',
    fill_color='BuPu',
    legend_name='하차',
).add_to(m)


# 지하철역 위치 데이터
station = pd.read_csv('./Daejeon_metro.csv',\
        names=['station','lat','lng'])

for i in range(1,len(station.values)):
    name = station.values[i][0]
    lat = station.values[i][1]
    lng = station.values[i][2]

    fl.Circle(location=[lat,lng], popup=name, fill='red', radius=400).add_to(m)

# 버스 정류장 위치 데이터
bus = pd.read_csv('./bus_station.csv',names=['no','name','city','district','dong','lng','lat'])
for i in range(1,len(bus.values)):
    bname = bus.values[i][1]
    blng = bus.values[i][5]
    blat = bus.values[i][6]

    fl.Circle(location=[blat,blng], popup=bname, color='#04B486', radius=5).add_to(m)
    print(bname, "\t", blat, '\t', blng)


# 버스 경로 그리기
route1 = pd.read_csv('./노선1_관저.csv',names=['no','name','city','district','dong','lng','lat'])
route1_coord = []
for i in range(1,len(route1.values)):
    blng = float(route1.values[i][5])
    blat = float(route1.values[i][6])
    route1_coord.append([blat,blng])

route2 = pd.read_csv('./노선2_구암동.csv',names=['no','name','city','district','dong','lng','lat'])
route2_coord = []
for i in range(1,len(route2.values)):
    blng = float(route2.values[i][5])
    blat = float(route2.values[i][6])
    route2_coord.append([blat,blng])

route3 = pd.read_csv('./노선3_순환.csv',names=['no','name','city','district','dong','lng','lat'])
route3_coord = []
for i in range(1,len(route3.values)):
    blng = float(route3.values[i][5])
    blat = float(route3.values[i][6])
    route3_coord.append([blat,blng])

fl.PolyLine(locations=route1_coord,color='red').add_to(m)
fl.PolyLine(locations=route2_coord,color='#E316B3').add_to(m)
fl.PolyLine(locations=route3_coord,color='#F8E303').add_to(m)

# 지도 데이터 출력
m.save('map.html')
webbrowser.open('map.html')