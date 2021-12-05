text = 'I am an NLPer'

def n_gram(text, n):
    return [text[idx:idx + n] for idx in range(len(text) - n + 1)] 

for i in range(1, 4):
    print(n_gram(text, i))
    print(n_gram(text.split(' '), i))