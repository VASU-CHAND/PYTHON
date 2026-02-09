
text = input("Enter a string: ")
result = ""

for ch in text:
    if ch >= 'a' and ch <= 'z':
        result = result + chr(ord(ch) - 32)
    else:
        result = result + ch

print("Uppercase string:", result)
