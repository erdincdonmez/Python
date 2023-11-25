def tahtaOlustur(boyuta,karaktera):

    # tahta = []
    # tahta = [[".",".",".",".",".",".",".",],
    #         [".",".",".",".",".",".",".",],
    #         [".",".",".",".",".",".",".",],
    #         [".",".",".",".",".",".",".",]
    #         ]

    
    for a in range(2):
        for b in range(2):
            tahta.insert([a][b],karaktera)
    
    # for a in range(boyuta):
    #     for b in range(boyuta):
    #         print(tahta[a][b])

    # for a in range(boyuta):
    #     print(karaktera*boyuta)

import random
def karakterYerlestir(gelen,boyutx):
    tahtaOlustur(boyutx,".")
    x = random.randint(0,boyut)
    y = random.randint(0,boyut)
    print(x,y,gelen)



boyut = 15
karakterYerlestir("O",boyut)