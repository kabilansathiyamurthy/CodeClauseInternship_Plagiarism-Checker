from difflib import SequenceMatcher
a = 'I Love Java'
b = 'I Like Python'
match = SequenceMatcher(None, a, b)
result = match.ratio() * 100
print(int(result), "%")