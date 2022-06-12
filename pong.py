#W - okno width
#H - okno height
W = 500
H = 500

#predkosc max pileczki
VMAX = 5

#zmienne dla paletek
#Width paletki
W_paletki = 10
#Height paletki
H_paletki = 100
#miejsce paletki na osi x
X_axis_l = 20  #dla lewej
X_axis_p = W - 20 - W_paletki #dla prawej
#miejsce paletki na osi y
Y_axis = H/2 - H_paletki/2

class Paletka():
    def __init__(self, x, y, szerokosc, wysokosc):
        self.x =self.og_x= x
        self.y= self.og_y=y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.predkosc = 5
    def reset(self):
        self.x = self.og_x
        self.y = self.og_y
        self.y_velocity = 0
        self.x_velocity*=-1        
    def draw(self, ekran):
        pygame.draw.rect(EKRAN, 'white',(self.x, self.y, self.szerokosc, self.wysokosc))

    def ruch(self, up=True):
        if up:
            self.y -= self.predkosc
        else:
            self.y += self.predkosc

class Pilka():
    def __init__(self, x, y, srednica):
        self.x = x
        self.y = y
        self.srednica = srednica
        self.x_v = VMAX
        self.y_v = 0

    def draw(self, ekran):
        pygame.draw.circle(ekran, 'white',(self.x, self.y), self.srednica)

    def ruch(self):
        self.x += self.x_v
        self.y += self.y_v

#fukcja odpowiadająca za poruszanie paletkami
def ruch_paletek():
    #dla paletki lewej, 'w' - up, 's' - down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if paletka_l.y - paletka_l.predkosc >= 0:
           paletka_l.ruch()
    elif keys[pygame.K_s]:
        if paletka_l.y + paletka_l.predkosc + paletka_l.wysokosc <= H:
           paletka_l.ruch(up=False)

    #dla paletki prawej, arrow up - up, arrow down - down
    if keys[pygame.K_UP]:
        if paletka_p.y - paletka_p.predkosc >= 0:
           paletka_p.ruch()
    elif keys[pygame.K_DOWN]:
        if paletka_p.y + paletka_p.predkosc + paletka_p.wysokosc <= H:
           paletka_p.ruch(up=False)

def kolizja(pilka, paletka):
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

    #else: kolizja dla prawej jest inna - trzeba tu napisac

    #printowanie koordynatow, zeby bylo prosciej debugowac
    print((pilka.x, pilka.y))
    

pilka = Pilka(W/2, H/2, 5)
paletka_l = Paletka(10, H/2-H_paletki/2, W_paletki, H_paletki)
paletka_p = Paletka(W-10-W_paletki, H/2-H_paletki/2, W_paletki, H_paletki)

