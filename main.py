def test_palindrome(input_value):
    s = str(input_value)
    if s == s[::-1]:
        return True
    else:
        return False