#!/usr/bin/env python3
#-*- coding : utf-8 -*-
def isleapyear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False;
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input())
month = int(input())
day = int(input())
daysofmonth = [31,28,31,30,31,30,31,31,30,31,30,31]

if isleapyear(year) == True:
    daysofmonth[1] = 29
sum = 0
for i in range(0,month - 1):
    sum += daysofmonth[i]
sum += day
print("sum is :",sum)