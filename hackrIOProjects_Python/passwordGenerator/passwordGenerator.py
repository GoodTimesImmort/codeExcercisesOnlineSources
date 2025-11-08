"""
File Name: passwordGenerator.py
Author: hackr.io
Reproduced: goodTimesImmort
Link: https://hackr.io/blog/python-projects
Description: This is a pasword generator thatblackjack game with text input and ASCII art.
[gT_I]: Creates a strong password by setting the conditinos and then looping with secrets and random until the conditions are met. It then prints the password.
"""

import secrets
import string

def create_pw(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False
    
    while not pw_strong:
        pwd = ''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))
        
        if (any(char in special_chars for char in pwd) and sum (char in digits for char in pwd) >= 2):
            pw_strong = True

    return pwd

if __name__ == '__main__':
    print(create_pw())