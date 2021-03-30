#!/usr/bin/python3
import datetime
lens = [10, 100, 1*1024, 2*1024, 4*1024]
for i in lens:
    print(f'{datetime.datetime.now()} - Message length: {i} - {"a"*i}')
for i in reversed(lens):
    print(f'{datetime.datetime.now()} - Message length: {i} - {"a"*i}')
