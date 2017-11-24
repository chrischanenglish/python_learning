#!/usr/bin/env python3
#-*-coding: utf-8-*-
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print('clock 1 : %s'% time.clock())
time.sleep(2)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print('clock 2 : %s'% time.clock())