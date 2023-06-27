# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 00:07:20 2023

@author: poros
"""

import matplotlib.pyplot as plt

import numpy

ctk1n = numpy.array([1,2,2,1,
                     2,    2,
                     1,2,2,1,])
ctk2n = numpy.array([0,0,0,0,
                     0,    0,
                     2,2,2,2])

ctkn = numpy.array([2/48,4/48,4/48,2/48,
                    4/48,          4/48,
                    6/48,8/48,8/48,6/48])
def newtk(x, y):
    
    tk = (x/ctk1n.sum())*ctk1n + (y/ctk2n.sum())*ctk2n
    return tk/tk.sum()
    
def makeData ():
    # Строим сетку в интервале от -10 до 10, имеющую 100 отсчетов по обоим координатам
    x = numpy.linspace (0.01, 3.01, 100)
    y = numpy.linspace (0.01, 3.01, 100)

    # Создаем двумерную матрицу-сетку
    xgrid, ygrid = numpy.meshgrid(x, y)
    # В узлах рассчитываем значение функции
    z = xgrid
    
    xgrid, ygrid = numpy.meshgrid(x, y)
    for i in range(len(x)):
        for j in range(len(y)):
            tk = newtk(x[i],y[j])
            for k in range(10):
                z[i][j]=(abs(tk[k] - ctkn[k]))
    return xgrid, ygrid, z
      

x,y,z = makeData()

fig = plt.figure()
axes = fig.add_subplot(111,projection='3d')

    # !!!
axes.plot_surface(x, y, z, cmap='inferno')
axes.view_init(25, 80)

plt.show()
