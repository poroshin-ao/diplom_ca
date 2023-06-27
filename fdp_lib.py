# -*- coding: utf-8 -*-
"""
Created on Dec 24 2020

@author: Федченко Дмитрий
@subject: Библиотека функций
"""
"""
1. Функция перевода целого числа в двоичный код
"""
def int_to_digits(n,x):
    rule = []
    while x > 0:
        rule.append(x % 2)
        x = x // 2
    while len(rule) < n:
        rule.append(0)
    return rule
"""
1.1 Функция перевода целого числа в двоичный код
"""
def int_to_digits_3bit(n,x):
    rule = []
    while x > 0:
        rule.append(x % 3)
        x = x // 3
    while len(rule) < n:
        rule.append(0)
    return rule
"""
2. Двоичный список переводим в целое (десятичное) число
"""
def digits_to_int(list):
    x = 0
    for j in range(len(list)):
        x += list[j] * 2**j
    return x
"""
3. Функция вероятности появления частицы на медиане правила rule
"""
def medium_probability(length, rule):
    cellular_automaton = draw_rule(length, rule)
    medium = len(cellular_automaton)
    medium_line = []
    particle = 0
    for i in range(medium):
        medium_line.append(cellular_automaton[i][medium])
        if cellular_automaton[i][medium] == 0:
            particle += 1
    particle_probability = particle / medium
    return particle_probability
"""
4. Функция прорисовки правила подавтомата
"""
def draw_sub_rule(length, rule_number):

    # Количество шагов автомата
    r = (length - 1)//2 - 1
    cellular_automaton = []
    tmp_list = []    
    row = []
    # Добавление частиц на нулевом шаге
    for l in range(length):
        if l != (length - 1) // 2: # and l != int(((length + 5) / 2)) and l != int(((length - 7) / 2)):
            row.append(0)
        else:
            row.append(1)
    cellular_automaton.append(row)    
    rule = int_to_digits(4, rule_number)
    # Работа КА по заданному правилу
    for k in range(r):
        tmp_list.append(0)
        for i in range(length - 2):
            tmp_list.append(rule[row[i] * 2**1 +
                                 row[i + 2] * 2**0])
        tmp_list.append(0)    
        cellular_automaton.append(tmp_list)
        row = list(tmp_list)
        tmp_list=[]
    return cellular_automaton
"""
5. Функция прорисовки правила
"""
def draw_rule(length, rule_number):

    # Количество шагов автомата
    r = (length - 1)//2 - 1
    cellular_automaton = []
    tmp_list = []    
    row = []
    # Добавление частиц на нулевом шаге
    for l in range(length):
        if l != (length - 1) // 2: # and l != int(((length + 5) / 2)) and l != int(((length - 7) / 2)):
            row.append(0)
        else:
            row.append(1)
    cellular_automaton.append(row)    
    rule = int_to_digits(8, rule_number)
    # Работа КА по заданному правилу
    for k in range(r):
        tmp_list.append(0)
        for i in range(length - 2):
            tmp_list.append(rule[row[i] * 2**2 +
                                 row[i + 1] * 2**1 +
                                 row[i + 2] * 2**0])
        tmp_list.append(0)    
        cellular_automaton.append(tmp_list)
        row = list(tmp_list)
        tmp_list=[]
    return cellular_automaton
"""
000 100 010 110 001 101 011 111
 0   1   1   1   0   1   1   0

6. Создание nxm матрицы из нулей
"""
def draw_field(n, m):
    field = []
    row = []
    for i in range(int(n)):
        for j in range(int(m)):
            row.append(0)
        field.append(row)
        row = []        
    return field
"""
7. Создание границы шириной в одну клетку и частицы с координатами (x,y)
"""
def draw_field_with_particle(n, m, x, y):
    field = draw_field(n, m)
    field[int(x)][int(y)] = 1
    #field[int(x)][int(y+1)] = 1
    #field[int(x+1)][int(y)] = 1
    #field[int(x+1)][int(y+1)] = 1
    return field
"""
8. Прорисовка границы в 1px
"""
def draw_border(n, m, field):
    # Прорисовка границы border = 1
    
    for i in range(n):
        for j in range(m):
            if i <= 1 or j <= 1 or i >= n - 2 or j >= m - 2:
                field[i][j] = 2
    """
    field[1][7] = 0
    field[1][6] = 0
    field[2][7] = 0
    field[2][6] = 0
    
    field[4][6] = 0
    field[2][5] = 2
    
    field[1][7] = 2
    field[2][7] = 2
    field[3][7] = 2
    
    field[2][3] = 2
    field[3][3] = 2
    
    field[3][6] = 2
    field[3][5] = 2
    field[5][3] = 2
    
    field[4][2] = 1
    field[6][2] = 1
    field[8][2] = 1
    field[10][2] = 1
    """
    """
    for i in range(n):
        for j in range(m):
            field[i][j] = ((i % 2) * (j % 2)) * 2
    #field[5][2] = 1
    #field[5][4] = 2
    field[10][10] = 1
    """

    field[12][10] = 2
    field[12][11] = 2
    field[12][12] = 2
    field[12][13] = 2
    field[12][14] = 2

    field[14][10] = 2
    field[14][11] = 2
    field[14][12] = 2
    field[14][13] = 2
    field[14][14] = 2
    
    field[10][10] = 2
    field[11][10] = 2
    field[12][10] = 2
    field[13][10] = 2
    field[14][10] = 2

    field[10][12] = 2
    field[11][12] = 2
    field[12][12] = 2
    field[13][12] = 2
    field[14][12] = 2

    return field
    