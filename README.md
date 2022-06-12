# pong
#projekt z programowania
class Menu():
def menu():
    dis.fill(BLACK)
    text("MAIN MENU", FONT, WHITE, screen, 20, 20)

    mx, my =pygame.mouse.get_pos()

    butt1 = pygame.Rect(50,100,200,50)
    butt2 = pygame.Rect(50, 200, 200,50)
    if butt1.collidepoint((mx, my)):
        if click:
            main()
    if butt2.collidepoint((mx, my)):
        if click:
            quit()

    pygame.draw.react(dis, WHITE, butt1)        
    pygame.draw.react(dis, WHITE, butt2) 

     click = False
     for event in pygame.event.get():
         if event.type== pygame.QUIT:
             pygame.quit()
             break
  #nie mam pojecia czy to ma jakis sens, jak komus sie uda cos z tym wymyslic to kupuje mu czekolade, bo ja nic nie czaje 
