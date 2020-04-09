#
# Created by Andrei Zhyunou on 2019-03-29.
#

import matplotlib.pyplot
import numpy
import io
from sympy import *
import sympy

data1 = io.BytesIO(open('input.txt', 'rb').read().replace(b',', b';').replace(b')', b' ').replace(b'(', b' ').replace(b'[', b' ').replace(b']', b' ').replace(b'^', b'**'))

y = numpy.genfromtxt(data1, dtype=(float, float, float, float, float, float, float, float, float, float, float, "|S50"), delimiter=";")

x = symbols('x')

f = []
z = []
result = []
result_0 = []

g = 9.8

for i in range(0, 3):
    x1 = y[i][0]
    y1 = y[i][1]
    x2 = y[i][2]
    y2 = y[i][3]
    Vx0 = y[i][4]
    Vy0 = y[i][5]
    V_x = y[i][6]
    V_y = y[i][7]
    t1 = y[i][8]
    t2 = y[i][9]
    t3 = y[i][10]
    equation = str(y[i][11])
    equation = equation.replace("'", '').replace('b', '').replace(' ', '')

    Vx = Vx0 + V_x
    Vy = Vy0 + V_y

    maxtime = Vy / g
    alltime = 2 * maxtime

    h = (Vy ** 2) / (2 * g) + y1

    if t1 >= alltime:
        Vx1 = 0
        Vy1 = 0
    else:
        if t1 > maxtime:
            Vy1 = g * t1 + Vy
        elif t1 == maxtime:
            Vy1 = 0
        elif t1 < maxtime:
            Vy1 = Vy - g * t1
        Vx1 = Vx

    if t2 >= alltime:
        Vx2 = 0
        Vy2 = 0
    else:
        if t2 > maxtime:
            Vy2 = g * t2 + Vy
        elif t2 == maxtime:
            Vy2 = 0
        elif t2 < maxtime:
            Vy2 = Vy - g * t2
        Vx2 = Vx

    if t3 >= alltime:
        Vx3 = 0
        Vy3 = 0
    else:
        if t3 > maxtime:
            Vy3 = g * t3 + Vy
        elif t3 == maxtime:
            Vy3 = 0
        elif t3 < maxtime:
            Vy3 = Vy - g * t3
        Vx3 = Vx

    Vx1 = round(Vx1, 2)
    Vy1 = round(Vy1, 2)
    Vx2 = round(Vx2, 2)
    Vy2 = round(Vy2, 2)
    Vx3 = round(Vx3, 2)
    Vy3 = round(Vy3, 2)
    h = round(h, 2)

    equation1 = (2 * Vx * Vy * (x - x1) - g * ((x - x1) ** 2)) / (2 * (Vx ** 2)) + y1
    equation = equation.replace('x', '*x')
    equation = sympify(equation)
    equation *= (-1)

    sol = solve(equation + equation1)

    for m in range(0, len(sol)):
        ko = sol[m]
        al = (2 * Vx * Vy * (ko - x1) - g * ((ko - x1) ** 2)) / (2 * (Vx ** 2)) + y1
        st = str(equation)
        st = st.replace('x', 'ko')
        st = sympify(st)
        st = solve(st)
        f.append(al)
        z.append(st[0])

        if (f[m] != x1 and f[m] != y1 and isinstance(f[m], sympy.numbers.Float) and isinstance(z[m], sympy.numbers.Float)):
            result.append(round(sol[m], 3))
            result.append(round(f[m], 3))

    count1 = -0.05
    count2 = -0.05
    x_hit = 0
    y_hit = 0

    while count1 <= 0.05:
        if result[0] + count1 == x2:
            x_hit == 1
        count1 += 0.01

    while count2 <= 0.05:
        if result[1] + count2 == y2:
            y_hit == 1
        count2 += 0.01
    if (x_hit == 1 and y_hit == 1):
        hit = 1
    else:
        hit = 0

    equation2 = equation1 - h
    solution = solve(equation2)

    solut = str(solution[0])
    counter = 0
    h_x = ""
    while counter < len(solut):
        if counter < 6:
            h_x = h_x + solut[counter]
        counter += 1

    h_x = float(h_x)

    if h > result[1] and h_x > result[0]:
        h = result[1]

    array = numpy.array(['(' + str(round(result[0], 2)) + ',' + str(round(result[1], 2)) + '); ' + str(
        round(h, 2)) + '; [' + str(Vx1) + ',' + str(Vy1) + ']; ' + '[' + str(Vx2) + ',' + str(Vy2) + ']; ' + '[' + str(
        Vx3) + ',' + str(Vy3) + ']; ' + str(hit)])
    result_0.append(result[0])
    result_0.append(result[1])
    if i == 0:
        array1 = array
        x_1 = numpy.linspace(x1, 2, 100)
        k1 = str(equation1)
    elif i == 1:
        array2 = array
        x_2 = numpy.linspace(x1, 2, 100)
        k2 = str(equation1)
    elif i == 2:
        array3 = array

        x_3 = numpy.linspace(x1, 2, 100)
        k3 = str(equation1)

equation = equation * (-1)

x = x_1
k_0 = eval(str(equation))
k_res = eval(k1)
matplotlib.pyplot.plot(x, k_0, label='Tereń')
matplotlib.pyplot.plot(x, k_res, label='Trajektoria')
matplotlib.pyplot.scatter(x2, y2, s=30, c='blue', label='Cel')
matplotlib.pyplot.scatter(result_0[0], result_0[1], s=30, c='red', label='Uderzenie')

matplotlib.pyplot.legend()
matplotlib.pyplot.savefig('1.png')
matplotlib.pyplot.show()

x = x_2

k_0 = eval(str(equation))
k_res = eval(k2)
p = matplotlib.pyplot.plot(x, k_0, label='Teren')

matplotlib.pyplot.plot(x, k_res, label='Trajektoria')
matplotlib.pyplot.scatter(x2, y2, s=30, c='blue', label='cel')
matplotlib.pyplot.scatter(result_0[2], result_0[3], s=30, c='red', label='Uderzenie')
matplotlib.pyplot.legend()
matplotlib.pyplot.savefig('2.png')
matplotlib.pyplot.show()

x = x_3

k_0 = eval(str(equation))
k_res = eval(k3)

matplotlib.pyplot.plot(x, k_0, label='Tereń')
matplotlib.pyplot.plot(x, k_res, label='Trajektoria')
matplotlib.pyplot.scatter(x2, y2, s=30, c='blue', label='Cel')
matplotlib.pyplot.scatter(result_0[4], result_0[5], s=30, c='red', label='Uderzenie')
matplotlib.pyplot.legend()
matplotlib.pyplot.savefig('3.png')
matplotlib.pyplot.show()

numpy.savetxt('output.txt', (array1, array2, array3), delimiter='', fmt="%s")
