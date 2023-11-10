# Python

## www

* [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
* [https://docs.python.org/](https://docs.python.org/)

## Data Types

### None

```python
nothing = None
if Nothhing is None:
    print(nothing)  # output: None
```

### Numeric Datatypes

#### int

* no limitation in size of number

```python
vdez = 1234
vokt = 0o2471
vhex = 0x5A3F
vbin = 0b1101

```
**bit operations:**

| operator  | operation |
| --------- | ---------------- |
| x & y     | AND |
| x \| y    | OR |
| x ^ y     | XOR |
| x << n    | shift n bits to left |
| x >> n    | shift n bits to right |


#### float

```python
a = 3.141
b = 3.141e-12  # -> 3.141 * 10^-12
print(3.0e999) # -> inf     (infinity)
```

#### bool

```python
v1 = True
v2 = False
```

**Operators:**
* not x
* x and y
* x or y

**Compare with not:**

| type      | False-value |
| --------- | ----------- |
| int       | 0           |
| float     | 0.0         |
| complex   | 0 + 0j      |
| str       | ""          |
| list      | []          |
| tuple     | ()          |
| dict      | {}          |
| set       | set()       |
| frozenset | frozenset() |

```python

if not "":
    print("empty string")
```

#### complex

```python
c = 2 + 4j

# c.real -> 2.0
# c.imag -> 4.0
```

#### Special Arithmetic Operators

```python
# residual part of division
print (8 % 3) # -> 2

# power
print (3 ** 3) # -> 27

# rounded quotien
print (10 // 3) # -> 3
```

**Augmented Assignments:**
* x += y -> x = x + y
* x -= y -> x = x - y
* x *= y -> x = x * y
* x /= y -> x = x / y

**Converting functions:**

* int()
* float()
* bool()
* complex()


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

## Loops

### while

```python
# while:
x = 0
while x < 10:
    print(x)
```

Use `break` to cancel whole loop, use `continue` to cancel current cycle and continue with next cycle.

### for

```python
for i in [1, 2, 3]:
    print(i)    #outpu: 1, 2, 3

# cool with range(start, stop, step)

for i in range(3):
    print(i)    # output: 0, 1, 2

for i in range(2, 11, 2):
    print(i)    # output: 2, 4, 6, 8, 10 
```

## pass

Use to replace code block not implemeted yet:

```python
if x == 1:
    pass
else:
    print("x too big!")
```


