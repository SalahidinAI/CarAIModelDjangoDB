a = dict(a='hello', b='hello2', c=22)
for i in a:
    elem = a[i]
    print(elem if type(elem) != str else 'sss')
