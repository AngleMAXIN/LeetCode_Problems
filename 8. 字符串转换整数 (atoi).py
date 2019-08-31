class Solution:
    def myAtoi(self, str: str) -> int:
        sign=1
        str=str.strip()
        if not str:
            return 0
        if str[0]=="+" or str[0]=='-':
            if str[0]=="-":
                sign=-1
            str=str[1:]
        ans=0
        for i in str:
            if i.isdigit():
                ans=ans*10+int(i)
            else:
                break
        ans=ans*sign
        if ans>2**31-1:
            return 2**31-1
        elif ans<-2**31:
            return -2**31
        else:
            return ans
        
s = Solution()

str = "+9128"

r = s.myAtoi(str)

print(r)
k  
