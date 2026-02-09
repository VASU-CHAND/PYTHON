s = input()
s = s.upper()

letters = {}

for ch in s:
    if ch.isalpha():
        if ch in letters:
            letters[ch] += 1
        else:
            letters[ch] = 1

for key in sorted(letters):
    print(str(letters[key]) + key)
