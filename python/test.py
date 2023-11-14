#!/usr/bin/env python3

import enum

class MyWeekday(enum.Enum):
    Monday: 1
    Tuesday: 2
    Wednesday: 3
    Thursday: 4
    Friday: 5
    Saturday: 6
    Sunday: 7
    
    
wd = MyWeekday.Monday


print(wd)
print(wd.name)
# -> 




