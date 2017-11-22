#!/usr/bin/env python3
#-*- coding: utf-8 -*-
profit = int(input())
bonus = 0
boundrys = [1000000, 600000, 400000, 200000, 100000, 0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]
for i in range(len(boundrys)):
    if profit > boundrys[i]:
        bonus += (profit - boundrys[i]) * rate[i]
        profit = boundrys[i]
print('bonus is',bonus)


