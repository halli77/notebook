# Python

## Data Types

```python
# integer:
i = 1
# float:
j = 1.05
# string:
k = "Hello World!"
# list:
l = ["A", "B", "C"]
# dictionary:
m = {"key1" : "value1", "key2" : "value2"}
```

## Shebang

* #!/usr/bin/env python3
* chmod +x "file"

## Code Lines
```python
# wrap line with "\"
s = "Hallo " \
    "Welt"

# merge commands to one line with ";"
print(a); print(b)
```

## if
Reminder: There is no switch/else keyword in python!

Standard syntax:
```python
if x == 1:
    print("x is 1")

if x > 1 and x < 2:
    print("x is between 1 and 2")

if x == 1:
    print("x is 1")
elif x == 2:
    print("x is 2")
elif x == 3:
    print("x is 3")
else:
    print("x is greater than 3")
```

Condtional expression
```python
var = (20 if x == 1 else 30)

# same as:
if x == 1:
    var = 20
else:
    var = 30
```
