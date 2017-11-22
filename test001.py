#!/usr/bin/env python3
#-*- coding: utf-8 -*-
d = []
for i in range(1,5):
    for j in range(1,5):
        if(i == j):
            continue
        for k in range(1,5):
            if (i != k) and (j != k):
                d.append([i,j,k])
print('total number is :', len(d))
for a in d:
    print(a)