class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()
        word = ""
        for i in s:
            if i.isalnum():
                word += i
        word = word.lower()
        listOfWord = list(word)
        backwordsWord = []
        for i in listOfWord:
            if i.isalpha():
                backwordsWord.insert(0, i)
            else:
                backwordsWord.append(i)
        print(listOfWord)
        print(backwordsWord)
        if listOfWord == backwordsWord:
            return True
        return False