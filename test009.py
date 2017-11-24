#!/usr/bin/env python3
#-*-coding: utf-8 -*-
import time

myD = {1:'a',2:'b'}
print(dict.items(myD))
for key,value in dict.items(myD):
    print(key,value)
    time.sleep(10)