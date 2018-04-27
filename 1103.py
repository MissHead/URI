while(True):
    str_split = input().split()
    
    h1,m1,h2,m2 = str_split

    h1 = int(h1)
    m1 = int(m1)
    m2 = int(m2)
    h2 = int(h2)
    
    if ((h1 + h2 + m1 + m2) == 0):
        break

    inicio = 0
    final = 0

    if (h1 == 0):
        h1 = 24
    
    inicio = h1 * 60 + m1
    
    if (h2 == 0):
        h2 = 24
    
    final = h2 * 60 + m2
    
    if (final > inicio):
        print (final - inicio)
    
    else:
        print (24 * 60 - (inicio - final))
