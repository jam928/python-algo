def santize(str):
    result = ""
    for i in range(len(str)):
        if not str[i].isalnum():
            continue
        result += str[i]
    return result.lower()

def is_palindrome(str):
    str = santize(str)
    for i,e in enumerate(str):
        if str[i] != str[len(str) - 1 - i]:
            return False

    return True
