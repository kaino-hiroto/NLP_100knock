def cipher(text):
    text2 = ''
    for w in text:
        if 97 <= ord(w) <= 122:
            text2 += chr(219 - ord(w))
        else:
            text2 += w    

    return ''.join(text2)

text = 'This is test.'
a = cipher(text)
print(a)
b = cipher(a)
print(b)