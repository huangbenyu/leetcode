
from functools import reduce
import operator

s ="abcd"
t ="abcde"

ss = map(ord,s+t)
print (s)
print(t)

print(list(ss))
#map(lambda x: x ** 2, [1, 2, 3, 4, 5])


tt= (reduce(operator.xor, map(ord, s+ t)))
print(tt)