#!/usr/bin/env python3
#-*- coding: utf-8 -*-
a = []
for i in range(3):
    a.append(int(input()))
for i in range(3):
    for j in range(i + 1, 3):
        if a[i] > a[j]:
            b = a[i]
            a[i] = a[j]
            a[j] = b
print('x is ',a[0])