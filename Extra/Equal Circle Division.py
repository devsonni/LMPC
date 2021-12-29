import math
import numpy as np
from math import pi, cos, sin

num_cuts = 25
angle = 0
x_p = np.zeros((num_cuts))
y_p = np.zeros((num_cuts))
radious = 320

for i in range(num_cuts):
    angle = i*(360/num_cuts)
    degree = (angle * pi / 180)
    x_p[i] = 0 + radious * cos(degree)
    y_p[i] = 0 + radious * sin(degree)
    print("X -> {}, Y-> {} \n".format(x_p[i],y_p[i]))
