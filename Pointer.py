num1 = 11

num2 = num1 # point to same address

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1)) # take the address id()
print("num2 points to:", id(num2)) 

num2 = 22 # integer are immutable, num2 point to new integer with different address

print("\nAfter num2 value is updated:") 
print("num1 =", num1) # 11 
print("num2 =", num2)  # 22

# different address
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


#####################################


dict1 = {
         'value': 11
        }

dict2 = dict1  # both variable point to same dict
# if no variable pointing to a dict, this dict will be removed by garbage collection mechanism

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2['value'] = 22 # not point to a new dict, just overwrite value

print("\nAfter value is updated:") 
print("dict1 =", dict1) # 22
print("dict2 =", dict2) # 22

print("\ndict1 points to:", id(dict1))# still same address
print("dict2 points to:", id(dict2))


