#!/usr/bin/env python3


r = (1, 2, 3) # -> tuple with 3 elements
s = (1,) # -> tuple with 1 element (watch the colon!)
t = () # -> empty tuple

birthdate = 29, 9, 2017
print(birthdate) # -> (29, 9, 2017) 

d, m, j = birthdate
print(d, m, j) # -> 29 9 2017

tu = (1, 2, 3, 4, 5, 6)
one, *middle, six = tu
print(one, middle, six) #-> 1 [2, 3, 4, 5] 6
