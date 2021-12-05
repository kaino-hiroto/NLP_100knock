text1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

text2 = text1.replace('.', '').replace(',', '')

a = [len(words) for words in text2.split()]
print(a)