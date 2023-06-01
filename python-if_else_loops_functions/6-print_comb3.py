#!/usr/bin/python3
for i in range(10, 99):
    for z in range(0, 9):
        for k in range(0, 9):
            if (i != z and z != k and i != k):
                print(i, )
