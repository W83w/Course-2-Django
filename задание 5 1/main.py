#import random

#List = []
#for i in range(10):
#    random_ = random.randint(50, 150)
#    List.append(random_)
#print(List)

#2
#import random

#randomElements = [50, 10, 34, 90, 76, 30]
#random.shuffle(randomElements)
#print(randomElements)


#def fanc_Degrees_in_Radians():
#    import math
#    X = math.radians(180)
#    print(X)
#fanc_Degrees_in_Radians()

#def fanc_Radians_in_degrees():
#    import math
#    X = math.degrees(math.pi)
#   print(X)
#fanc_Radians_in_degrees()

import math

#Sin = []
#for a in range(181):
#   Sin.append(math.sin(math.radians(a)))
#print(Sin)


import math

import math


def circle_length(radius): # длина окружности через радиус
    return 2 * math.pi * radius
print(circle_length(10), 'длина окружности через радиус')

def circle_area(radius): # площадь
    return math.pi * radius * radius
print(circle_area(10), 'площадь круга через радиус')