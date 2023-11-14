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

| Operator  | Operation |
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

| Operator           | Description                                                         |
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

#### list

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

#### tuple - the immutable list

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


#### str, bytes, bytearray

```python
s = "Hello world"
t = ("Hello world, "
     "how is it going?")
print(t) # -> Hello world, how is it going?

b = b"i am bytes"
print(b) # -> b'i am bytes'

barray = bytearray(b'i am bytearray')
print(barray) # -> bytearray(b'i am bytearray')
```

##### Splitting Strings

| Method                    | Description                                                                    |
| ------------------------- | ------------------------------------------------------------------------------ |
| s.split([sep, maxsplit])  | Splitting s at sep                                                             |
| s.rsplit([sep, maxsplit]) | Splitting s at sep, but reverse                                                |
| s.splitlines([keepends])  | Splitting s at crlf                                                            |
| s.partition(sep)          | Splitting s at first occurance of sep, returns 3-tuple (split, sep, remainder) |
| s.rpartition(sep)         | see above                                                                      |

##### Search Strings

| Method                      | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| s.find(sub, [start, end])   | search for sub in s and returns index                 |
| s.rfind(sub, [start, end])  | reverse find()                                        |
| s.index(sub, [start, end])  | like s.find, but throws exception if sub is not found |
| s.rindex(sub, [start, end]) | reverse rindex()                                      |

##### Replace Strings

| Method                       | Description                                                                       |
| ---------------------------- | --------------------------------------------------------------------------------- |
| s.replace(old, new, [count]) | replaces all occurances of old with new, optionally limited to count replacements |
| s.lower()                    | converts string to lower case                                                     |
| s.upper()                    | converts string to upper case                                                     |
| s.swapcase()                 | inverts upper and lower case                                                      |
| s.capitalize()               | first char upper case, remaining chars lowercase                                  |
| s.casefold()                 | like lower(), but additionally replaces special characters                        |
| s.title()                    | first char of every word to upper case, remaining chars to lower case             |
| s.expandtabs([tabsize])      | replaces tabs by tabsize numbers of blanks                                        | 

##### Adjust Strings

| Method                      | Description                                      |
| --------------------------- | ------------------------------------------------ |
| s.center(width, [fillchar]) | center string                                    |
| s.ljust(width, [fillchar])  | adjust to left                                   |
| s.rjust(widht, [fillchar])  | like s.ljust                                     |
| s.zfill(with)               | fill "numeric" strings with zeros from left side |


##### Test Strings

| Method                             | Description                                      |
| ---------------------------------- | ------------------------------------------------ |
| s.isalnum()                        | True if s contains only letters or digits        |
| s.isalpha()                        | True if s contains only letters                  |
| s.isdigit()                        | True if s contains only digits                   |
| s.islower()                        | True if s contains only lower case letters       |
| s.isupper()                        | True if s contains only upper case letters       |
| s.isspace()                        | True if all letters are blanks                   |
| s.istitle()                        | True if all words in s begin with a upper letter |
| s.startswith(prefix, [start, end]) | True if s begins with prefix                     |
| s.endswith(suffix, [start, end])   | True if s ends with suffix                       |



##### Connect Strings

| Method      | Description                                                         |
| ----------- | ------------------------------------------------------------------- |
| s.join(seq) | concats all elements of seq to a new string, s is used as separator |

```python
seq = ["www", "github", "com"]

print(", ".join(seq)) # -> www, github, com
print(".".join(seq))  # -> www.github.com
print("".join(seq))   # -> wwwgithubcom
```


##### Format Strings

```python
print("It's {hour}:{minute}.".format(hour=14, minute=30)) 
# -> It's 14:30.

print("It's {};{}.".format(14, 30))
# -> It's 14:30.

c = 10 + 5j
print("Real part: {0.real}, imaginary part: {0.imag}".format(c))
# -> Real part: 10.0, imaginary part: 5.0

print("Sum: {:.2f} EUR".format(12.3753))
# -> Sum: 12.38 EUR

print("Binary: {:b}".format(99))
# -> Binary: 1100011

print("per cent: {:%}".format(0.25))
# -> per cent: 25.000000%

```

### Dictionary

* key/value pairs
* like associative array in PHP or map in C++

```python
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
    
```

#### Operators

| Operator   | Description                       |
| ---------- | --------------------------------- |
| len(d)     | number of elements in d           |
| d[k]       | gets value of key k in d          |
| del d[k]   | delets key/value pair with key k  |
| k in d     | True if d contains key k          |
| k not in d | Truef if d does not contain key k |


#### Methods

| Method                      | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| d.clear()                   | empty d                                                            |
| d.copy()                    | returns a copy of d                                                |
| d.get(k, [x])               | returns value of k if exists, else x                               |
| d.items()                   | returns iterable object containing all key/value pairs             |
| d.keys()                    | returns iterable object containing all keys                        |
| d.pop(k)                    | returns value of k and deletes k from d                            |
| d.popitem()                 | returns randon key/value pair and delets it from d                 |
| d.setdefault(k, [x])        | add k/x if not exists, and allways returns value of k              |
| d.update(d2)                | adds d2 to d and overwrites possible duplicates in d               |
| d.values()                  | returns iterable object containg all values                        |
| dict.fromkeys(seq, [value]) | creates new dictionary with seq als keys and as value for each key |


### set, frozenset

* every element must be unique
* s = set()
* s1 = { 1, 2, 3}
* fs = frozenset()
* fs2 = frozenset([3, 4, 5])

#### Operators

| Operator | Description                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| len(s)   | number of elements in s                                                       |
| x in s   | True if s contains x                                                          |
| s <=t    | True if s is subset of t                                                      |
| s < t    | True if s is genuine subset of t (-> there is at least one more element in t) |
| s \| t   | returns a new set containing the elements of both sets s and t (merge)        |
| s & t    | returns a new set with all elements containted in s as well as in in t        |
| s - t    | returns a new set with elements from s, but not from t                        |
| s ^ t    | returns a new set with elements from s or from t, but not in both             |


#### Methods

| Method                    | Description                                                |
| ------------------------- | ---------------------------------------------------------- |
| s.issubset(t)             | like s <= t                                                |
| s.issuperset(t)           | like s >= t                                                |
| s.isdisjoint(t)           | True if s and t have no common elements                    |
| s.union(t)                | like s \| t                                                |
| s.intersection(t)         | like s & t                                                 |
| s.difference(t)           | like s - t                                                 |
| s.symmetric_difference(t) | like s ^ t                                                 |
| s.copy()                  | returns a copy of s                                        |
| s.add(e)                  | add e to s                                                 |
| s.clear()                 | deletes all elements from s                                |
| s.discard(e)              | deletes e from s and does not throw an error if e not in s |
| s.remove(e)               | like discard(), but throws exception of e not in s         |


## Modules

### time 

* [https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html)
* contains time.struct_time (t = time_strut_time((2023, 11, 22, 18, 25, 59, 0, 0 0)))

| Function                   | Description                                                   |
| -------------------------- | ------------------------------------------------------------- |
| asctime([t])               | converts t (time.struct_time) into string                     |
| perf_counter()             | returns time for performance measuring                        |
| ctime([sec])               | converts unix ts into string                                  |
| gmtime([sec])              | converts unit ts into struct_time using UTC                   |
| localtime([sec])           | like gmtime, but with local time                              |
| mktime(t)                  | converts struct_time into unix ts using local time            |
| sleep(sec)                 | pauses program for sec seconds                                |
| strftime(format, [t])      | converts struct_time into string unsing given format commands |
| strptime(string, [format]) | converts string into struct_time                              |
| time()                     | returns current unix ts using UTC                             |


### datetime, timedelta

* [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)
* datatypes: date, time, datetime, timedelta

```python
import time
import datetime

d = datetime.date(2022, 11, 23)
# d = datetime.datetime.today()
# -> 2022-11-23

print(datetime.date.timetuple(d))
# -> time.struct_time(tm_year=2022, tm_mon=11, tm_mday=23, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=327, tm_isdst=-1)

t = datetime.time(2, 30, 59)
print(t)
# -> 02:30:59

dt = datetime.datetime(2022, 11, 23, 2, 30, 59)
# dt = datetime.datetime.now()
# dt = datetime.datetime.utcnow()
# -> 2022-11-23 02:30:59

unix_ts = time.time()
dt = datetime.datetime.fromtimestamp(unix_ts)
# -> 2023-11-14 08:27:54.433735

d1 = datetime.datetime(2023, 10, 23, 0, 0, 0)
d2 = datetime.datetime(2023, 10, 24, 1, 0, 0)
delta1 = d2-d1
print("difference:", delta1)
# -> difference: 1 day, 1:00:00
print ("difference in days:", delta1.days)
# -> difference in days: 1
print ("difference in seconds:", delta1.seconds)
# -> difference in seconds: 3600
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


