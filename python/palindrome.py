def isPalindrome(s):
    """
    Assumes s is a string, returns true if string is a palindrome
    """
    def toAlpha(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters += c
        return letters

    def isPalindrome(s):
        if len(s) <= 1:
            return True
        else:
            answer = s[0] == s[-1] and isPalindrome(s[1:-1])
            return answer
    return isPalindrome(toAlpha(s))

print(isPalindrome('yo')) # => False
print(isPalindrome('yoy')) # => True