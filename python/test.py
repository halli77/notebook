#!/usr/bin/env python3


d1 = {"DE" : "Germany", "CH" : "Switzerland", "AT" : "Austria"}

d2 = {
     "DE" : "Germany", 
     "CH" : "Switzerland", 
     "AT" : "Austria"
     }

# dict comprehension
d3 = { i: i*i for i in range(5) }
print(d3) # -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16} 

for key in d1:
    print("{} -> {}".format(key, d1[key]))
    # DE -> Germany
    # CH -> Switzerland
    # AT -> Austria
    
    
for x in d1.items():
    print("k: {x[0]} -> v: {x[1]}".format(x))