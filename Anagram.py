# Program to verify if the given string is Anagram or not

s1 = input("Enter the first String = ")
s2 = input("Enter the second String = ")

if sorted(s1) == sorted(s2):
    print("Entered String is Anagram")
else :
    print("Entered String is not Anagram")
