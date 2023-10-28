# Write your code here
text = input("Put in a word: ")
count = int(input("Enter how many letters (at the end) you want to alter: "))
firstPart = text[:-(count)]
lastPart = text[-(count):]
transformed = lastPart.upper()
print(firstPart + transformed)

# Write your code here
excerpt = input("Type an excerpt: ")
substr = input("What are you trying to find in the excerpt: ")
excerpt2 = excerpt.lower()
substr = substr.lower()
excerpt2 = excerpt2.strip()
substr = substr.strip()
count = excerpt2.count(substr)
print("Sentence: ", excerpt)
print("Word to look for in sentence: ", substr)
print(f"There are {count} occurrences of '{substr}' in the sentence.")
