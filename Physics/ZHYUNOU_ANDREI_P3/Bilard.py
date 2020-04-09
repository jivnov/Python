#
# Created by Andrei Zhyunou on 2019-04-18.
#

import numpy
import io
from sympy import *
import matplotlib.pyplot

data1 = io.BytesIO(open('input.txt', 'rb').read().replace(b',', b';').replace(b')', b' ').replace(b'(', b' ').replace(b'[', b' ').replace(b']', b' '))

data = numpy.genfromtxt(data1, dtype=(float, float, float, float, float, float), delimiter=";")

Array = []

R = 0.03
r = 0.05
m = 0.017
miu = 0.015
d = 0.1
l = 2.7
h = 1.35
g = 9.81

counter = 2
count_band_b = mo = 0

for il in range(0, counter):

    x0 = data[il][0]
    y0 = data[il][1]
    V0x = data[il][2]
    V0y = data[il][3]
    x2 = data[il][4]
    y2 = data[il][5]

    a_pred = miu * g
    V0 = sqrt((V0x ** 2) + (V0y ** 2))
    t = V0 / a_pred
    t = float(t)
    res_x = res_y = res_x2 = res_y2 = []
    i = 0.001
    alpha = k = z = 1
    im = 2
    b = p = 0
    N1 = N2 = N3 = 0
    testing = 0.03
    V_dx = V_dy = 0
    count = 0

    faul = score = buck_y = buck_x = change = False

    while i <= t:
        x = x0 + V0x * i + (a_pred * (i ** 2)) / 2
        y = y0 + V0y * i + (a_pred * (i ** 2)) / 2

        if not buck_y:
            if y > k * 1.35:
                buck_y = change = True
                k += 1
            else:
                y = y - b * 1.35

        if buck_y:
            y = y * (-1) + k * 1.35
            if y < 0:
                buck_y = False
                change = True
                k += 1
                b += 2

        if not buck_x:
            if x > z * 2.7:
                buck_x = change = True
                z += 1
            else:
                x = x - p * 2.7

        if buck_x:
            x = x * (-1) + z * 2.7
            if x <= 0:
                buck_x = False
                change = True
                z += 1
                p += 2

        if change:
            if x < 0:
                x = x * -1
            if y < 0:
                y = y * -1
            x = round(x, 1)
            y = round(y, 1)
            N2 += 1
            change = False

        if x >= 2.7 - (r - R) and y >= 1.35 - (r - R) or x >= 2.7 - (r - R) and y <= 0 + (r - R) or x <= 0 + (
                r - R) and y >= 1.35 - (r - R) or x <= 0 + (r - R) and y <= 0 + (r - R) or y <= 0 + (
                r - R) and 1.35 - (r - R) <= x <= 1.35 + (r - R) or y >= 1.35 - (r - R) and 1.35 - (
                r - R) <= x <= 1.35 + (r - R):
            faul = True
            break

        if N2 > mo:
            v_new = sqrt((V0 ** 2) * 0.7)
            t = v_new / a_pred
            mo += 1
        res_x.append(x)
        res_y.append(y)

        if i == 0.001:
            x01 = x
            y01 = y
        i += 0.001

    matplotlib.pyplot.figure(figsize=(15, 8))
    matplotlib.pyplot.scatter(res_x, res_y, 1)
    matplotlib.pyplot.scatter(x01, y01, color='blue', label='Poczatkowe polozenie bili')
    matplotlib.pyplot.scatter(x, y, color='black', label='Koncowe polozenie bili')
    matplotlib.pyplot.scatter(x2, y2, color='red', label='Polozenie bili')
    matplotlib.pyplot.hlines(y=1.35, xmin=0.05, xmax=1.3, color='r')
    matplotlib.pyplot.hlines(y=1.35, xmin=1.4, xmax=2.65, color='r')
    matplotlib.pyplot.hlines(y=0, xmin=0.05, xmax=1.3, color='r')
    matplotlib.pyplot.hlines(y=0, xmin=1.4, xmax=2.65, color='r')
    matplotlib.pyplot.vlines(x=0, ymin=0.05, ymax=1.3, color='r')
    matplotlib.pyplot.vlines(x=2.7, ymin=0.05, ymax=1.3, color='r')
    pictures = ""
    pictures = str(il + 1) + '.png'
    matplotlib.pyplot.savefig(pictures)
    x = str(round(x, 1))
    y = str(round(y, 1))
    x2 = str(round(x2, 1))
    y2 = str(round(y2, 1))
    if faul == False:
        array = numpy.array(['(' + x + ',' + y + '); (' + x2 + ',' + y2 + '); ' + ' ' + str(N1) + '; ' + str(
            N2) + '; ' + str(N3) + ';'])
    elif faul == True:
        array = numpy.array(['(faul); (' + x2 + ',' + y2 + '); ' + ' ' + str(N1) + '; ' + str(N2) + '; ' + str(N3) + ';'])
    Array.append(array)
numpy.savetxt('output.txt', (Array[0], Array[1]), delimiter='', fmt="%s")
