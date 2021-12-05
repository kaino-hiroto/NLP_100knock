text1 = 'paraparaparadise'

text2 = 'paragraph'

def n_gram(text, n):
    return [text[idx:idx + n] for idx in range(len(text) - n + 1)] 

X = n_gram(text1, 2)
Y = n_gram(text2, 2)

print(f'和集合: {set(X) | set(Y)}')
print(f'積集合: {set(X) & set(Y)}')
print(f'差集合: {set(X) - set(Y)}')
print('se' in (set(X) & set(Y)))