# Problem Statement:
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!


SENTENCE_START = "In the world of programming, there was a "

def mad_libs():
    adjective = input("Enter an adjective (describing word): ")
    noun = input("Enter a noun (tech-related thing/person): ")
    verb = input("Enter a verb (coding action): ")

    sentence = (f"{SENTENCE_START} {adjective} {noun} that {verb} !")   
    print(sentence) 

mad_libs()

# output:
# Enter an adjective (describing word): intelligent
# Enter a noun (tech-related thing/person): programmer
# Enter a verb (coding action): enjoying
# In the world of programming, there was a  intelligent programmer that enjoying !



