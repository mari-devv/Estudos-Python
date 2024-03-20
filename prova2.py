a = 10
b = 6

for i in range(6):
    # i = 0 logo ele adiciona 3 ao "a" - 13
    if i % 3 == 0: 
        a = a + 3
    #    
    elif i % 2 == 0:
        a = a + 2
    else:
        a = a + 1

print(a)