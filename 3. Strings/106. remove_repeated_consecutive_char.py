# 106. Write a ptyhon program to remove repeated consecutive characters and replace them with single letters and print a pdated string

def test(text):
  result = []
  for x in text:
    if not result or result[-1] != x:
      result.append(x)
  return ''.join(result)

text ="Red Green White"
print("Original string:", text)
print("Remove repeated consecutive characters and replace with the single letters:")
print(test(text))