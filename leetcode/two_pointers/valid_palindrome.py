def is_palindrome(s: str) -> bool:
    def sanitize(str):
        result = ""
        for i in range(len(str)):
            if not str[i].isalnum():
                continue
            result += str[i]
        return result.lower()

    s = sanitize(s)
    for i, e in enumerate(s):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True


print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
print(is_palindrome(" "))  # True
