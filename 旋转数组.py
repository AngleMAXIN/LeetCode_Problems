# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
     def minNumberInRotateArray(self, rotateArray):
        # write code here
        low = rotateArray[0]
        start = 0
        end = len(rotateArray) - 1
        res = low
        while start <= end:
            mid = (start+end) // 2
            if rotateArray[mid] > low:
                start = mid+1
            else:
                end = mid -1
            # elif rotateArray[mid] < low and rotateArray[mid-1] > rotateArray[mid]:
            #      res = rotateArray[mid]   
            #      break
    
        return min(rotateArray[start],rotateArray[end])

# class Solution:
#     def minNumberInRotateArray(self, target, rotateArray):
#         # write code here

#         start = 0
#         end = len(rotateArray) - 1
#         res = 0
#         while start <= end:
#             mid = (start+end) // 2
#             print("---",start, mid,end)
#             if rotateArray[mid] > target:
#                 end = mid -1
#             elif rotateArray[mid] < target:
#                 start = mid+1
#             else:
#                 res = mid
#                 break
#             # elif rotateArray[mid] < low and rotateArray[mid-1] > rotateArray[mid]:
#             #      res = rotateArray[mid]   
#             #      break
#         return res



arr = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
s = Solution()
r = s.minNumberInRotateArray(arr)
print("index:",r)
