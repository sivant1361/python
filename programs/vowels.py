import re

def search_vowel(str):
    pattern=r"[aeiou]"
    if re.search(pattern,str):
        print("Vowels are found:)")
    else:
        print("Vowels not found:(")

str=input("Enter a string:")
search_vowel(str)