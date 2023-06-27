# -*- coding: utf-8 -*-
"""
Created on Fri May 26 05:37:51 2023

@author: poros
"""
import numpy as np
import matplotlib.pyplot as plt

def ruletobin(rule):
    rulebin = []
    for i in range(8):
        rulebin.append(rule%2)
        rule = rule//2
    return np.array(rulebin)
    
def masofrule(rule, IS):
    rulebin = ruletobin(rule)
    l = len(IS)
    mas = np.zeros([(l-1)//2+1, l+(l-1)])
    mas[0,(l-1)//2:l+(l-1)//2] = IS
    for i in range((l-1)//2):
        for j in range(1,2*l-2):
            n = mas[i,j-1:j+2]

            mas[i+1,j] = rulebin[int(n[0]*4+n[1]*2+n[2])]
    return mas[:,(l-1)//2:l+(l-1)//2]

IS = np.zeros(51)
IS[25] = 1
mas = masofrule(30,IS)

fig, ax = plt.subplots()
im = ax.imshow(mas)
plt.imshow(mas)    