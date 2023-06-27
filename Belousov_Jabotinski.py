# -*- coding: utf-8 -*-
"""
Created on Fri May 26 09:30:59 2023

@author: poros
"""

import numpy as np
import matplotlib.pyplot as plt

def to_next(a,b):
    A = (a+1)%3
    n = 0
    for i in b:
        if i == A:
            n = n+1
    if(n>2):
        return A
    return a

def bel_jab(itr,n):
    #mas = np.random.randint(0,3,[n,n])
    mas = np.zeros([n,n]) 
    """
    mas[40:50:1,0:50:1] = 1
    mas[50:60:1,50:99:1] = 2
    mas[40:50:1,50:99:1] = 1
    mas[50:60:1,0:50:1] = 2
    """
    #mas[50:60:1,50:60:1] = 1
    mas[50:60:1,50:60:1] = 2
    mas[50:60:1,40:50:1] = 1
    nmas = np.zeros([n,n])
    for it in range(itr):
        for i in range(n):
            for j in range(n):
                nmas[i,j] = to_next(mas[i,j],[mas[i,j-1], mas[i, (j+1)%n], mas[i-1,j], mas[(i+1)%n,j],
                                              mas[i-1,j-1], mas[i-1,(j+1)%n], mas[(i+1)%n,j-1], mas[(i+1)%n,(j+1)%n]])
        mas = np.array(nmas)
        fig, ax = plt.subplots()
        im = ax.imshow(mas)
        plt.imshow(mas)   

bel_jab(200,100)
