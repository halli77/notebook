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



### Sequential datatypes

* list, tuple, str, bytes, bytearray

#### operators

| operator           | description                                                         |
| ------------------ | ------------------------------------------------------------------- |
| x in s             | True if x is contained in s                                         |
| x not in s         |                                                                     |
| s + t              | new sequence containingg s and t                                    |
| s * n              | new sequence containing n copies of s                               |
| s[i]               | get i'th element of s                                               |
| s[i:j]             | get elements between i and j                                        |
| s[i:j:k]           | get every k'th element between i and j                              |
| len(s)             | get number of elements in s                                         |
| max(s)             | get biggest element of s                                            |
| min(s)             | get smallest element of s                                           |
| s.index(x[, i, j]) | get index of first occurance of x in s (optionally between i and j) |
| s.count(x)         | how often is x countained in s                                      |

**Examples:**

```python
l = "-"
line = 10*l
print(line) # -> ----------

a = "hello "
b = "world"
a += b
print(a) # -> hello world

l0 = [1, 2, 3]
l1 = [4, 5, 6]
l2 = l0 + l1
print(l2) # -> [1, 2, 3, 4, 5, 6]
print(max(l2)) # -> 6
print(min(l2)) # -> 1
print(3 in l2) # -> True
print(3 in l1) # -> False
print(l0[2]) # -> 3
print(l0[-1]) # -> 3
print(b[1:4]) # -> orl
print(len(l2)) # -> 6
print(b.index("l")) # -> 3
print("hello world".count("l")) # -> 3
```

### list

* is mutable
* elements can be of different datatypes

| Operator   | Description                                |
| ---------- | ------------------------------------------ |
| s[i] = x   | replace element at i with x                |
| s[i:j] = t | replace elements at i:j with t             |
| del s[i]   | delete element i                           |
| del s[i:j] | delete elements betwenn i and j, j remains |

| Method                 | Description                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------- |
| s.append(x)            | appends x to end of s                                                                                     |
| s.extend(t)            | appends all elements of t to s                                                                            |
| s.insert(i, x)         | inserts element x at i and shifts remaining items to right                                                |
| s.pop([i])             | returns i'th element and deletes it from s; if i is not set, pop returns last element                     |
| s.remove(x)            | deletes first occurance of x in s                                                                         |
| s.reverse()            | reverses the order of s                                                                                   |
| s.sort([key, reverse]) | sorts s. if given a function as key parameter (i.e. "len"), sort applies the funtion to every member of s |

### tuple - the immutable list

Operators of lists (but not methods) can be used for tuples as well.

```python
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

Condtional expression:

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


