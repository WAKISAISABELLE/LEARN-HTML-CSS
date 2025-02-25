#write program to  calculate length of string.
'''
string = input("Enter a string:")
length = len(string)
print(length)
'''

#character frequency
sample_string = 'google.com'
char_freq = {}
for char in sample_string:
    char = char.lower()
if char.isalnum():#ignoring spaces and punctuation.
    if char in char_freq:
        char_freq[char] +=1
    else:
        char_freq[char] = 1
print("Character frequencies:") 
for char, freq in char_freq.items():
    print(f"{char}:{freq}")

