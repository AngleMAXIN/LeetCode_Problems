#二维数组的查找

class Solution:
    def Find(self, t, a):
        # write code here
        gao = len(a)
        hang = len(a[0]) - 1 
        # a[0][hang]
        x = 0
        while hang >= 0 and x < gao:
            cur=a[x][hang]
            print cur,x,hang
            if cur > t:
                hang -= 1
            elif cur < t:
                x += 1
            else:
                return True
        return False
        
target = 7
arrary = [[1,2,8,9],\
         [4,7,10,13]]

s = Solution()
r = s.Find(target,arrary)
print r