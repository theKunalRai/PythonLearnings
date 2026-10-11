""" Program to convert a given string into lowercase,
uppercase, capital and title case string using comprehension
"""
sentence = input("Enter a sentence: ")
# lowercase = sentence.lower()
# uppercase = sentence.upper()
# capital = sentence.capitalize()
# titled = sentence.title()

# print("Lowercase sentence: ",lowercase)
# print("Uppercase sentence: ",uppercase)
# print("Capitalized sentence: ",capital)
# print("Titled sentence: ",titled) """

lowercases = "".join(char.lower() for char in sentence)
uppercases = "".join(char.upper() for char in sentence)
capitalcases = "".join(char.capitalize() for char in sentence[0:1]) + "".join(char.lower() for char in sentence[1:])
titledcases = " ".join(word[0].upper() + "".join(char.lower() for char in word[1:]) for word in sentence.split())


print("Lowercase sentence: ", lowercases)
print("Uppercase sentence: ", uppercases)
print("Capitalized sentence: ", capitalcases)
print("Titled sentence: ",titledcases)