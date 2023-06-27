# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:34:05 2020

@authors: Дмитрий Федченко, Иван Тимофеев
"""
import fdp_lib
import matplotlib.pyplot as plt

def create_field():
    stream = open('field_tk.txt', 'r')
    tmp = stream.readlines()
    field = []
    for i in range(len(tmp)):
        row = []
        for j in range(len(tmp[0]) - 1):
            row.append(int(tmp[i][j]))
        field.append(row)
    return field

def wcode_neumann(d, r,
                  rule_code_one,
                  rule_code_two,
                  rule_code_three,
                  rule_code_four, steps):
    
    code_digits = d ** r
    
    field = create_field()
    
    rule_one = fdp_lib.int_to_digits_3bit(code_digits, rule_code_one)
    rule_two = fdp_lib.int_to_digits_3bit(code_digits, rule_code_two)
    rule_three = fdp_lib.int_to_digits_3bit(code_digits, rule_code_three)
    rule_four = fdp_lib.int_to_digits_3bit(code_digits, rule_code_four)
    
    fig, ax = plt.subplots()
    plt.imshow(field)
    
    plt.show()
    
    path = []
    l = len(field)
    
    for i in range(l):
        path_row = []
        for j in range(len(field[i])):
            path_row.append(field[i][j] % 2)
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
        
        #fig, ax = plt.subplots()
        #plt.imshow(field)
        
        # filename = 'CA_' + str(k) + '.png'
        # fig.savefig(filename, format = 'png', dpi = 500)
        # fig, ax = plt.subplots()
    
    im = ax.imshow(path)
    fig.colorbar(im, ax=ax)
    plt.imshow(path)
    #fig.savefig('path.png', format = 'png', dpi = 500)
    
    # for j in range(len(path)):
    #     print(path[j])
    
    return path
    
# create_field()

wcode_neumann(3, 5, 
                87189642485960958202911070585860771696858196300629529285884717025707245184955461514567350134642761960475397463135221,
                87189642485960958202911070585860771696865629006937516856646420535307083748847009511688466704807114187492178155124653, 
                87189642485960958202911070585860771696865758879240222128254776164230511032271591445048493784239863824054082719415381, 
                87189642485960958202911070585860771696865758879493973628716181482036815078820525046538331816246773325439025350595533,
                15)

