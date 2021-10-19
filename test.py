'''from cv2 import imread
from pyzbar.pyzbar import decode as qr_read

distance = lambda x1, y1, x2, y2: ((x2 - x1)**2 + (y2 - y1)**2)**0.5
navigate = lambda x, y: print(f'navigate(x={x}, y={y})')
     
image = imread("QR_test1.png")
barcode = qr_read(image)
data = barcode[0].data.decode("utf-8")
data_con = data.split('\n')
start = [int(i) for i in data_con[0].split(',')]
finish = [int(i) for i in data_con[1].split(',')]
color = data_con[-1].strip()
xyColor = []
s = 0
for i in range(1, int(data_con[2])+1):
    line = data_con[2+i+s].split(',')
    if line[1].strip() != color:
        s += int(line[0])
        continue
    k = int(line[0])
    for j in range(1,k+1):
        xyColor.append([int(c) for c in data_con[2+i+s+j].split(',')])
    s += k
    
navigate(*start)
for i in range(len(xyColor)):
     distanceAll = [distance(*start, *xy) for xy in xyColor]
     minDistance = min(distanceAll)
     k = distanceAll.index(minDistance)
     xy = xyColor[k]
     navigate(*xy)
     del xyColor[k]
navigate(*finish)
print('land()')
'''

import networkx as nx
import matplotlib.pyplot as plt

dist = lambda x, y: ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5


start = list(map(int, input().split()))
finish = list(map(int, input().split()))
Point = {}
Point['start'] = start.copy()
Point['finish'] = finish.copy()
color = {}
for i in range(int(input())):
    k, c = input().split()
    xy = []
    for j in range(int(k)):
        xy.append(list(map(int, input().split())))
    color[c] = xy
colorGo = input()

G = nx.Graph()
plt.text(*start, 'start')
plt.text(*finish, 'finish')
for i in range(len(color[colorGo])):
    text = colorGo + str(i+1)
    x, y = color[colorGo][i]
    Point[text] = [x, y]
    plt.text(x, y, text)
for i in Point:
    for j in Point:
        if i == j or i[1] == j[1]:
            continue
        G.add_edge(i, j, weight=dist(Point[i], Point[j]))
plt.show()
