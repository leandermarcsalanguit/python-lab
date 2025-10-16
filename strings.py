print("Hello! This is a string.")

x = "This is a string assigned to a variable."
print(x)                                            # You can print strings this way too.

y = """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua."""
print(y)                                            # This is a multiline string. This can be done with three single ''' or double quotes """

stringArray = "Strings are also arrays."            # Strings can be treated like arrays
print(stringArray[0])

print("\n")                                         # You can print a new line by using "\n"

for i in "Loops":                                   # Looping through a string
    print(i)

length_ = "123456789"
print("The length of this string is" , len(length_))

sampleText = "Is the word python in this text?"
print("python" in sampleText)                       # This returns a boolean value, it checks whether the character/s are present in the string.

if "python" in sampleText:
    print("Yes, 'python' is in sample text.")       # This would only print if the given character/s or word/s are present.

if "Python" not in sampleText:                      # This is to check if character/s are present on a string. 
    print("No, 'Python is not in the text'")        # It is case-sensitive, therefore, 'Python' is different from 'python'