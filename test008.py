#!/usr/bin/env python3
#-*-coding: utf-8 -*-
for i in range(9):
    for j in range(i + 1):
        if j == i:
            print('%d*%d=%d'%(i+1,j+1,((i+1)*(j+1))))
        else:
            print('%d*%d=%d ' % (i+1,j+1,((i+1)*(j+1))),end='')