
s = "Python"
text = "I like Python"
text1 = "   ABC   "
print(s[0])
print(s[-1])
print(s.upper())
print(s.lower())

new_text = text.replace("Python", "java")
print(new_text)
print(text1.strip())
splited_text = text.split(" ")
print(splited_text)
joined = " - ".join(splited_text)
print(joined)