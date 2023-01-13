from turtle import *

num_sides = input()

num_sides = int(num_sides)

side_length = (100/int(num_sides))*10

if num_sides is range(3,5):
    side_length=100

angle = 360/int(num_sides)

s = getscreen()

for i in range(int(num_sides)):
    forward(side_length)
    right(angle)
