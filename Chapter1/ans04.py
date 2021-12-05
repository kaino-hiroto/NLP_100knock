text1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

text2 = text1.replace('.', '').replace(',', '')

def pick_up(i, w):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return (w[0], i)
    else:
        return (w[:2], i)    

a = [pick_up(i, words) for i, words in enumerate(text2.split(), 1)]
print(a)