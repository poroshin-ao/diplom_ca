# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 18:17:23 2023

@author: poros
"""

import numpy as np
import matplotlib.pyplot as plt

def to_next(a,b):
    A1 = (a+1)%5
    A2 = (a+2)%5
    n1 = 0
    n2 = 0
    for i in b:
        if i == A1:
            n1 = n1+1
        if i == A2:
            n2 = n2+1
    
    if(n1>2 and n2 >2):
        if (n1>=n2): return A1 
        else: return A2
    if n1>2: return A1
    if n2>2: return A2
    return a

def bel_jab(itr,n):
    mas = np.random.randint(0,5,[n,n])
    """mas = np.zeros([n,n])
    mas[50:100:1,50:60:1] = 3
    mas[50:100:1,40:50:1] = 4
    mas[0:50:1,40:50:1] = 1
    mas[0:50:1,50:60:1] = 2
    """
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