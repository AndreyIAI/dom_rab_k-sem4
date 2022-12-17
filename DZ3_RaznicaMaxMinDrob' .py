arr = [1.1, 1.2, 3.1, 5, 10.01]
arr = [x for x in arr if type (x) == float]
arr_float = list()

for i in arr: 
    arr_float.append(round(i % 1, 5))

print(max(arr_float)-min(arr_float))