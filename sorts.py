def Qsort(nums,r,l):
    if r < l:
        part = partition(nums,r,l)
        Qsort(nums,r,part-1)
        Qsort(nums,part+1,l)
    return nums 
def partition(nums,left,right):
    low = left
    high = right
    # 取最右边的元素
    cmp = nums[left]

    while low < high:
        while high > low and nums[high] >= cmp :
            high -= 1
       
        while high > low and nums[low] <= cmp:
            low += 1
        
        nums[high] ,nums[low] = nums[low], nums[high]
        nums[low] = cmp
    # nums[low],nums[r-1] = nums[low],nums[r-1]
    return low 


li = [5,7,98,9,93,53]
r = Qsort(li,0,len(li)-1)
print(r)

# def parttion(v, left, right):
#     key = v[left]
#     low = left
#     high = right
#     while low < high:
#         while (low < high) and (v[high] >= key):
#             high -= 1
#         
#         while (low < high) and (v[low] <= key):
#             low += 1
#         v[high] = v[low]
#         v[low] = key
#     return low
# def quicksort(v, left, right):
#     if left < right:
#         p = parttion(v, left, right)
#         quicksort(v, left, p-1)
#         quicksort(v, p+1, right)
#     return v

# s = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
# print("before sort:",s)
# s1 = quicksort(s, left = 0, right = len(s) - 1)
# print("after sort:",s1)