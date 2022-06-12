import pygame, sys
import time

pygame.init()
pygame.display.set_caption('PONG')
#W - okno width
#H - okno height
W = 500
H = 500
#Width paletki
W_paletki = 20
#Height paletki
H_paletki = 100
#predkosc max pileczki (potrzebna do kolizji z paletka)
VMAX = 5
EKRAN=pygame.display.set_mode((W,H))
zegar=pygame.time.Clock()
czcionka = pygame.font.SysFont("arial", 35)
wynik_l = 0
wynik_r = 0

class Paletka():
    def __init__(self, x, y, szerokosc, wysokosc):
        self.x = x
        self.y = y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.predkosc = 5

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

    def draw(self, ekran):
        pygame.draw.circle(ekran, 'white',(self.x, self.y), self.srednica)

    def ruch(self):
        self.x += self.x_v
        self.y += self.y_v

    def reset(self):
        self.x = W/2
        self.y = H/2

def wynik(pilka, paletka):
    global wynik_l
    global wynik_r
    if pilka.x >= W:
        pilka.reset()
        time.sleep(1)
        pilka.x_v = VMAX
        pilka.y_v = 0
        wynik_l += 1
        print(f"{wynik_l}:{wynik_r}")
    if pilka.x <= 0:
        pilka.reset()
        time.sleep(1)
        pilka.x_v = -VMAX
        pilka.y_v = 0
        wynik_r += 1
        print(f"{wynik_l}:{wynik_r}")

    if wynik_l == 10:
        wygrana = czcionka.render("Gracz 1 wygrał", 1, "white")
        EKRAN.blit(wygrana, (W/2 - wygrana.get_width()/2, 50))
        pygame.display.update()
        time.sleep(3)
        wynik_l = 0
        wynik_r = 0

    if wynik_r == 10:
        wygrana = czcionka.render("Gracz 2 wygrał", 1, "white")
        EKRAN.blit(wygrana, (W/2 - wygrana.get_width()/2, 50))
        pygame.display.update()
        time.sleep(3)
        wynik_l = 0
        wynik_r = 0


#funkcja, która obsługuje kolizje
def kolizja(pilka, paletka):
    #kolizja dla pilki i scian (lewa i prawa sciana tylko na potrzeby testowania)
    if pilka.y >= H:
        pilka.y_v *= -1
    if pilka.y <= 0:
        pilka.y_v *= -1

    #kolizja dla paletki i pilki
    #kolizja dla lewej
    if pilka.x_v < 0:
        if pilka.y >= paletka_l.y and pilka.y <= paletka_l.y + H_paletki:
            if pilka.x - pilka.srednica <= paletka_l.x + W_paletki:
                pilka.x_v *= -1
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

    else:
        if pilka.y >= paletka_p.y and pilka.y <= paletka_p.y + H_paletki:
            if pilka.x + pilka.srednica >= paletka_p.x:
                pilka.x_v *= -1
                srodek_paletki = paletka_p.y + H_paletki/2
                roznica_y = srodek_paletki - pilka.y
                max_roznica_y = H_paletki/2
                pilka.y_v = -(roznica_y/(max_roznica_y/VMAX))

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

#przypisywanie elementów klasom
pilka = Pilka(W/2, H/2, 5)
paletka_l = Paletka(10, H/2-H_paletki/2, W_paletki, H_paletki)
paletka_p = Paletka(W-10-W_paletki, H/2-H_paletki/2, W_paletki, H_paletki)

#główna pętla - obsluguje gre
while True:
    zegar.tick(60)
    EKRAN.fill('black')
    pilka.draw(EKRAN)
    paletka_l.draw(EKRAN)
    paletka_p.draw(EKRAN)
    pilka.ruch()
    wynik(pilka, paletka_l)
    #pokazuje wynik na ekranie
    wynik_show = czcionka.render(f"{wynik_l}:{wynik_r}", 1, "white")
    EKRAN.blit(wynik_show, (W/2 - wynik_show.get_width()/2, 20))
    ruch_paletek()
    kolizja(pilka, paletka_l)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
