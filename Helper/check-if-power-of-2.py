# check if a number is power of 2
g = 3

def isPowerOfTwo(g):
    while g % 2 == 0:
        g //= 2
    return g == 1

print(isPowerOfTwo(g))
# 3: 0011 2: 0010  3 & 2 = 0010=2
# 2: 0010 1: 0001  2 & 1 = 0000=0
# 4: 0100 3: 0011  4 & 3 = 0000=0
g & (g - 1) == 0 # check g is power of 2
print(g & (g - 1) == 0)



# int.bit_count() count the number of 1 in binary representation
# example: 
print(6 .bit_count()) # 110 -> 2
# if it is power of 2, there is only one 1 in binary representation
# 4: 0100 8: 1000 2: 0010 16: 10000