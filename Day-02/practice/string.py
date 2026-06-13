text = "Hello, My name is Saravjeet Singh"
# findText = "is"
findText = "not"
if findText in text:
    print("Text found", findText)
else:
    print("Text not found")

print(len(text))
print(text.upper())
print(text.lower())

str1 = "        hello     with     spaces         "
strippedText = str1.strip()
print(strippedText)

substringText = text[1:3]  ##[start, end] start included and end excluded
print(substringText)

text = "Python is awesome"
words = text.split()
print("Words:", words) #returns an array of split strings
##########################################3



