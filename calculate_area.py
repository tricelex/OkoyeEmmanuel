"""Calculate Area of a circle"""
import math

radius = int(input())
radius_square = math.pow(radius, 2)
area = math.ceil(math.pi * radius_square)

print(area)
