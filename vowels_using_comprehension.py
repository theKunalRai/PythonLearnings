""" #!Program to extract vowels form a given string and print
#! them in the same order as they are originally
"""
word = input("Enter a word: ")
vowels = "aeiouAEIOU"

vowels = "".join(char for char in word if char in vowels)
print("Vowels in the word:", vowels)