from math import pi

def area():
    length = int(input('What is the length (ft) of your house?: '))
    width = int((input('What is the width (ft) of your house?: ')))
    area = length * width
    return (f"The area of your house is {area}sq ft")

def circ():
    r = int(input('To calculate the circumference of a circle, please provide the radius : '))
    circumference = 2*pi*r
    return (f"The cirle's circumference is {circumference}")

print(pi)