import pygame, sys

width=800
height=400
dis= pygame.display.set_mode((width, height))


gracz1= pygame.image.load()
gracz2= pygame.image.load()

WHITE=(255, 255, 255)
BLACK=(0,0,0)
fps = 60
FONT= pygame.font.SysFont("arial", 35)
pygame.display.set_caption("pong")

def draw_window(dis, PKTright, PKTleft):
    dis.fill(BLACK),
#czcionka
    PKTleft_font = FONT.render(f"{PKTleft}",1, WHITE)
    PKTright_font = FONT.render(f"{PKTright}",1, WHITE)
#umiejscowienie punktow
    dis.blit(PKTleft, (WIDTH//4- PKTleft_font.getwidth()//2, 20))
    dis.blit(PKTright, (WIDTH* (3/4)- PKTright_font.getwidth()//2, 20))

    dis.blit(gracz1,(0, 0), gracz2,(780,390))
    pygame.display.update()



def main():
    clock= pygame.time.Clock()

    PKTleft=0
    PKTright=0

    run = True
    while run:

        
        clock.tick(fps)

        draw(dis, [leftpaddle, rightpaddle] ball, PKTleft, PKTright)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
#dodawanie punktow 
        draw_window(dis)
     if ball.x<0:
         PKTright+=1
    elif ball.x>width:
        PKTleft+=1
    pygame.quit()




if __name__ =="__main__":
    main()

pygame.init()

