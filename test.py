#!/usr/bin/python3
import datetime
lens = [10, 100, 10*1024, 20*1024]
for i in lens:
    print(f'{datetime.datetime.now()} - Message length: {i} - {"a"*i}')
for i in reversed(lens):
    print(f'{datetime.datetime.now()} - Message length: {i} - {"a"*i}')
