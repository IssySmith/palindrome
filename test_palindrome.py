from main import is_palindrome

def palindrome_true():
    assert is_palindrome(121) == True
    
def palindrome_false():
    assert is_palindrome(122) == False