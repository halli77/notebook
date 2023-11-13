#!/usr/bin/env python3


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
