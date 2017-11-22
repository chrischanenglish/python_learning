#!/usr/bin/env python3
#-*- coding: utf-8 -×-
for i in range(2,85,2):
    if 168 % i == 0:
        j = 168 / i
        if j % 2 != 0:
            continue
        if i > j:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n ** 2 - 100
            if x > 0:
                print('%d' %x)


