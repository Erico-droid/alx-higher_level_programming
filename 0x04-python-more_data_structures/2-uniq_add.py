#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    rezult = 0
    for i in new:
        rezult += i
    return rezult
