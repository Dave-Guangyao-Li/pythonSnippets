'''
https://www.bigocheatsheet.com/

best: omega, average:theta, worst:omicron

n = 1,000
O(1) = 1 constant
O(logn) = 10
O(n) = 1,000 proportional
O(nlogn) = 10,000 Divide and conquer
O(n^2) = 1,000,000 loop within a loop

O(2^n)
O(n!)
'''

# different terms for inputs:  O(a*b) not O(n)
def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print_items(1, 10)