def is_palindrome(input_v):
    s = str(input_v).lower()
    s = s.replace(" ", "")
    if s == s[::-1]:
        return True
    else:
        return False