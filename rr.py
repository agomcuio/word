a = input('')
if len(a) % 2 != 0:
    x = int(len(a) / 2)
    xy = a[x]
    print(xy)
else:
    x = int(len(a) / 2)
    xy = a[x:x+2]
    print(xy)
    