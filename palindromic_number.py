def is_palindrome(num:int) -> bool:
    num = str(num)
    return num[::] == num[::-1]

is_palindrome2(16461)
