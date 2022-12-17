#Proizvedeniye
#VARIANT 1
# arr=[2,3,4,5,6]
# len_list = 0
# if len(arr) % 2 == 0:
#     len_list=len(arr)//2
# else:
#      len_list = len(arr) // 2+1

# for i in range(len_list):
#     print(arr[i] * arr [len(arr)-i-1])

#Variant2
arr=[2,3,4,5,6]

for i in range(len(arr) // 2+1):
    print(arr[i] * arr [len(arr)-i-1])
