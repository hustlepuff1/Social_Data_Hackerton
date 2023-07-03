import webbrowser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./대전 버스 10진.csv', encoding = 'utf-8')

import folium
from folium import plugins
m = folium.Map(location = [36.3504, 127.3845], zoom_start=5,width="%100",height="%100")
location=df[["위도","경도"]]
plugins.MarkerCluster(location).add_to(m)

minimap = plugins.MiniMap()
m.add_child(minimap)

m.save('map.html')
webbrowser.open('map.html')
