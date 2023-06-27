# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:59:53 2023

@author: poros
"""
import numpy as np


def ruletobin(rule, c):
    rulebin = []
    for i in range(c+1):
        rulebin.append(rule%c)
        rule = rule//c

    return np.array(rulebin)

def bintorule(rule,c):
    l = len(rule)
    n = 0
    for i in range(l-1,-1,-1):
        n = n + rule[i]*c**(l-1 - i)
    return n

def ruleforanyv(v):
    n = v + 2
    c = v + 1 
    rule = []
    
    for i in range(c**n):
        rb = ruletobin(i, c)
        if rb[-2] == 0:
            for k in range(-3,-(n+1),-1):
                if rb[k] != 0:
                    if rb[k] == -k-2:
                        
                        rule.insert(0,min(rb[k]+1,v))
                        break
                    elif rb[-1]!=0:
                        rule.insert(0,-k-2)
                        break
            if len(rule) != i+1:
                rule.insert(0,0)
        else:
            if rb[-1]!= 0:
                rule.insert(0,1)
            else:
                rule.insert(0,0)
    print(bintorule(rule, c))
    
ruleforanyv(3)
                
                            
    