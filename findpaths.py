# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:02:52 2023

@author: poros
"""

import fdp_lib
import matplotlib.pyplot as plt

def create_field():
    stream = open('field.txt', 'r')
    tmp = stream.readlines()
    field = []
    for i in range(len(tmp)):
        row = []
        for j in range(len(tmp[0]) - 1):
            row.append(int(tmp[i][j]))
        field.append(row)
    return field


def create_field_cars():
    stream = open('field_cars.txt', 'r')
    tmp = stream.readlines()
    field = []
    for i in range(len(tmp)):
        row = []
        for j in range(len(tmp[0]) - 1):
            row.append(int(tmp[i][j]))
        field.append(row)
    return field

def wcode_neumann_paths(d, r,
                  rule_code_one,
                  rule_code_two,
                  rule_code_three,
                  rule_code_four, steps):
    
    code_digits = d ** r
    
    field_o = create_field()
    field_cars = create_field_cars()
    
    rule_one = fdp_lib.int_to_digits_3bit(code_digits, rule_code_one)
    rule_two = fdp_lib.int_to_digits_3bit(code_digits, rule_code_two)
    rule_three = fdp_lib.int_to_digits_3bit(code_digits, rule_code_three)
    rule_four = fdp_lib.int_to_digits_3bit(code_digits, rule_code_four)

    mas_cars = []
    
    for i in range(len(field_cars)):
        for j in range(len(field_cars[0])):
            if(field_cars[i][j]==1):
                mas_cars.append([i,j])
    
    l = len(field_o)
    
    paths = []
    c_cars = []
    
    #fig, ax = plt.subplots()
    #plt.imshow(field_o)

    
    for g in mas_cars:
        
        field = []
        for i in range(l):
            field.append(list(field_o[i]))

        field[g[0]][g[1]] = 1  
        path = []
    
        for i in range(l):
            path_row = []
            for j in range(l):
                path_row.append(0)
            path.append(path_row)    

        for k in range(steps):
            tmp_field = []
            for i in range(l):
                tmp_row = []
                for j in range(l):
                    h = \
                        ((field[i % l][j % l] % 3) * 3**4
                         + (field[(i - 1) % l][j % l] % 3) * 3**3
                         + (field[i % l][(j - 1) % l] % 3) * 3**2
                         + (field[(i + 1) % l][j % l] % 3) * 3**1
                         + (field[i % l][(j + 1) % l] % 3) * 3**0)
                
                    #Код Вольфрама
                    tmp_row.append(int(0 == k % 4) * ((1 - (i + j + k) % 2) * rule_three[h] + ((i + j + k) % 2) * rule_one[h]) +
                                   int(1 == k % 4) * ((1 - (i + j + k) % 2) * rule_four[h] + ((i + j + k) % 2) * rule_two[h]) +
                                   int(2 == k % 4) * ((1 - (i + j + k) % 2) * rule_one[h] + ((i + j + k) % 2) * rule_three[h]) +
                                   int(3 == k % 4) * ((1 - (i + j + k) % 2) * rule_two[h] + ((i + j + k) % 2) * rule_four[h]))
               
                    path[i][j] += field[i][j] % 2    
            
                tmp_field.append(tmp_row)
            field = list(tmp_field)
            
            if field[g[0]][g[1]] == 1 and (k+1)%4==0:
                break
        
            #fig, ax = plt.subplots()
            #plt.imshow(field)
        
            # filename = 'CA_' + str(k) + '.png'
            # fig.savefig(filename, format = 'png', dpi = 500)
            # fig, ax = plt.subplots()
        
        #fig, ax = plt.subplots()
        #im = ax.imshow(path)
        #fig.colorbar(im, ax=ax)
        #plt.imshow(path)
        
        flag = 1
        
        for i in range(len(paths)):
            flag = 0
            for j in range(l):
                for k in range(l):
                    if paths[i][j][k] != path[j][k]:
                        flag = 1
                        break
                if flag == 1: break
            if flag == 0:
                c_cars[i].append(g)
                break
        
        if flag == 1:
            paths.append(path)
            c_cars.append([g])
    
    for i in range(len(paths)):
        fig, ax = plt.subplots()
        im = ax.imshow(paths[i])
        fig.colorbar(im, ax=ax)
        plt.imshow(paths[i])
        
        #print(c_cars[i])

    return paths, c_cars     
    
                
    #fig.savefig('path.png', format = 'png', dpi = 500)
    
    # for j in range(len(path)):
    #     print(path[j])
    
    
# create_field()

wcode_neumann_paths(3, 5, 
                87189642485960958202911070585860771696858196300629529285884717025707245184955461514567350134642761960475397463135221,
                87189642485960958202911070585860771696865629006937516856646420535307083748847009511688466704807114187492178155124653, 
                87189642485960958202911070585860771696865758879240222128254776164230511032271591445048493784239863824054082719415381, 
                87189642485960958202911070585860771696865758879493973628716181482036815078820525046538331816246773325439025350595533,
                200)