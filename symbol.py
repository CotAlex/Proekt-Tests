a = input()
numb = "0123456789"
alph = "qwertyuiopasdfghjklzxcvbnmёйцукенгшщзхъфывапролджэячсмитьбю"
s = list(a)
text = "Это не цифра и ни буква"
k = 0
l = 0
for i in s :
    if i in numb :
        text = "Это цифра"
        k += 1
    if i in alph :
        text = "Это буква"
        l += 1
if l > 0 and k > 0 :
    text = "Это не цифра и ни буква"
print(text)

