"""
Author: Rajendhiran Easu
Date: 25 August 2026
Description: 
"""

# import array
#
# # typecode - data types (must be b, B, u, w, h, H, i, I, l, L, q, Q, f or d)
# data = array.array('i', [11, -124, 52, 42])
# for va in data:
#     print(va)


from copy import copy, deepcopy

# without copy -- all values are reference the same (nested inner list and outer value)
first_data = [1, 2, 3, [4, 5], 6]
f1= first_data
f1.append(7)
f1[2]= 33
f1[3].append(4)
print(first_data)
print(f1)

# with copy (Shallow copy) -- outer list is new, only nested inner list values are share the same reference.
first_data = [1, 2, 3, [4, 5], 6]
f1= copy(first_data)
f1.append(7)
f1[2]= 33
f1[3].append(4)
print(first_data)
print(f1)

# # with copy (Deep copy) -- No reference, gives complete new object and new changes won't reflect.
first_data = [1, 2, 3, [4, 5], 6]
f1 = deepcopy(first_data)
f1.append(7)
f1[2] = 33
f1[3].append(4)
print(first_data)
print(f1)
