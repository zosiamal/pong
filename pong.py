def kolizja(pilka, paletka_l, paletka_p):
    #kolizja dla pilki i scian (lewa i prawa sciana tylko na potrzeby testowania przed implementacja punktacji)
    if pilka.x >= W:
        pilka.x_v *= -1
        print("kolizja_x")
    if pilka.x <= 0:
        pilka.x_v *= -1
        print("kolizja_x")
    if pilka.y >= H:
        pilka.y_v *= -1
        print("kolizja_y")
    if pilka.y <= 0:
        pilka.y_v *= -1
        print("kolizja_y")

    #kolizja dla paletki i pilki
    #kolizja dla lewej paletki
    if pilka.x_v < 0:
        if pilka.y >= paletka_l.y and pilka.y <= paletka_l.y + H_paletki:
            if pilka.x - pilka.srednica <= paletka_l.x + W_paletki:
                pilka.x_v *= -1
                print('kolizja_paletka')
                srodek_paletki = paletka_l.y + H_paletki/2
                #im wieksza roznica w y, tym wieksza predkosc pilki, max 5
                roznica_y = srodek_paletki - pilka.y
                max_roznica_y = H_paletki/2
                #roznica y ma zakres od 0 do 50
                #to 10 razy mniej niz vmax, to taka tymczasowa implementacja
                #wychodzi rowno od 0 do 5 (nowa predkosc)
                #chodzi o to, ze nowa predkosc musi byc z zakresu od 0 do VMAX
                #dlatego te dzialania skomplikowane, dziwne
                pilka.y_v = -(roznica_y/(max_roznica_y/VMAX))
                print(f'nowa predkosc: {pilka.y_v}')
                
#kolizje dla prawej paletki
    else:
        if pilka.y >= paletka_p.y and pilka.y <= paletka_p.y + H_paletki:
            if pilka.x + pilka.srednica >= paletka_p.x:
            pilka.x_v *= -1
            print('kolizja_paletka')

            srodek_paletki = paletka_p.y + H_paletki/2
            roznica_y = srodek_paletki - pilka.y
            max_roznica_y = H_paletki/2
            pilka.y_v = -(roznica_y/(max_roznica_y/VMAX))
            print(f'nowa predkosc: {pilka.y_v}')

    #printowanie koordynatow, zeby bylo prosciej debugowac
    print((pilka.x, pilka.y))
