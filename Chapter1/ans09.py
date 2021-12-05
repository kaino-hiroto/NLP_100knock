import random

def random_shuffle(word):
    if len(word) <= 4:
        return word
    else:
        begin = word[0]
        end = word[-1]
        other_words = random.sample(list(word[1:-1]), len(word[1:-1]))
        return ''.join([begin] + other_words + [end]) 

text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
a = [random_shuffle(word) for word in text.split()]
print(''.join(a))