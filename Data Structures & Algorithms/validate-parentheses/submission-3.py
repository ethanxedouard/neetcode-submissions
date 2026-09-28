class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        key = {"(":")", "[":"]", "{":"}"}

        for char in s:
            if char in key:
                ans.append(char)

            if char in key.values():
                if len(ans) < 1:
                    return False
                elif char == key.get(ans[-1]):
                    ans.pop()
                elif char != key.get(ans[-1]):
                    return False
                

        if len(ans) >= 1:
            return False
        else:
            return True
