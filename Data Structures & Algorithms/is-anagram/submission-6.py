class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = dict()
        t_hash = dict()

        if len(s) == len(t):
            for i in s:
                if i not in s_hash:
                    s_hash[i] = 1
                s_hash[i] += 1 

            for i in t:
                if i not in t_hash:
                    t_hash[i] = 1
                t_hash[i] += 1 

            if s_hash == t_hash:
                return True

        return False
        
