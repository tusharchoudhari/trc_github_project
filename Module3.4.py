from math import radians, sin, cos, acos

print("Please provide coordinates of two points:")
slat = radians(float(input("Star latitude: ")))
slon = radians(float(input("End longitude: ")))
elat = radians(float(input("Start latitude: ")))
elon = radians(float(input("End longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is",dist)