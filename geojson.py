from area import area
import math
import json
import sys,os
#import geojson
def segments(poly):
        return zip(poly, poly[1:] + [poly[0]])
tron=sys.argv[1]
with open(tron) as json_file:
    myfile = json.load(json_file)
areafile=myfile["features"]
a2=areafile[0]
a3=a2["geometry"]

print(p)
a4=a3["coordinates"]
a5=a4[0]
t=abs(sum(math.hypot(x0-x1,y0-y1) for ((x0, y0), (x1, y1)) in segments(a5)))
print('Perimeter of the json file is:')
t=t*100000
print(t)
print('Compactness is:')
comp=((4*3.14159)*p)/(t*t)
print(comp)

