def isPalindrome(number):
    return int(str(number)[::-1])==number

#print(isPalindrome(number=000))

def isPalindromeWord(word):
    #return True if word == word[::-1] else False
    return word == word[::-1]

#print(isPalindromeWord("kobyłamamałybok"))

def Palindrome(word):
    beginIndex = 0
    endIndex = len(word) - 1
    while beginIndex <= endIndex:
        if word[beginIndex] != word[endIndex]:
            return False
        else:
            beginIndex +=1
            endIndex -=1
    return True

#print(Palindrome("anna"))