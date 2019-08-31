class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)

        if l == 0:
            return True
        if l == 1 or l % 2 != 0:
            return False

        str_stack = []
        re_str = {"{": "}", "(": ")", "[": "]"}

        for _str in s:
            if _str in re_str:
                str_stack.append(_str)
            elif not str_stack:
                return False
            else:
                if re_str[str_stack[-1]] != _str:
                    return False
                str_stack.pop()

        return not str_stack


s = Solution()

strline = "()"

result = s.isValid(strline)

print(result)
