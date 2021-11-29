import pygame

#Button Texts
t1 = 'Send I/O'


driver_State = 0



#Colours used for deviceDriverAndController
bg_colour = (0, 129, 167)
colour1 = (253, 252, 220)
orange = (252, 191, 73)
outline_colour = orange
WHITE = (255,255,255)
BLACK = (0,0,0)
Maxim_Red = (214, 40, 40)
magenta = (255,0,255)
peach = (254, 217, 183)
bitter = (240, 113, 103)





def clean(window,label, box_label, small_label): # Clear prev state, get things set up
    window.fill(bg_colour) # bg colour
    DMA_title = label.render('Device Driver and Controller', 1, WHITE)  # Make label for title
    window.blit(DMA_title, (140, 40))  # show DMA_title label at relevant spot

    initial_Structure(window, box_label, small_label)

def initial_Structure(window, label, small):

    box1 = pygame.Rect(50, 350, 150, 100)
    box2 = pygame.Rect(250, 350, 150, 100)
    box3 = pygame.Rect(450, 350, 150, 100)
    box4 = pygame.Rect(640, 250, 100, 300)
    box5 = pygame.Rect(440, 340, 170, 120)



    pygame.draw.rect(window, peach, box5)
    pygame.draw.rect(window, colour1, box1)
    pygame.draw.rect(window, colour1, box2)
    pygame.draw.rect(window, colour1, box3)
    pygame.draw.rect(window, colour1, box4)


    t2 = label.render('Device', 1, BLACK)  # Make label for title
    window.blit(t2, (100, 390))  # show device label at relevant spot
    t3 = label.render('Device Controller', 1, BLACK)  # Make label for title
    window.blit(t3, (260, 390))  # show controller label at relevant spot
    t4 = label.render('Device Driver', 1, BLACK)  # Make label for title
    window.blit(t4, (475, 390))  # show driver label at relevant spot
    t5 = label.render('OS', 1, BLACK)  # Make label for title
    window.blit(t5, (680, 390))  # show OS label at relevant spot
    t6 = small.render('I/O System', 1, BLACK)  # Make label for title
    window.blit(t6, (500, 338))  # show OS label at relevant spot

    t1 = 'Send I/O'

def draw_connections(window):

    global t1

    box6 = pygame.Rect(200, 400, 50, 10)
    box7 = pygame.Rect(400, 400, 40, 10)
    box8 = pygame.Rect(610, 400, 30, 10)



    if driver_State > 2:
        pygame.draw.rect(window, bitter, box6)
        t1 = 'Receive I/O'

    if driver_State > 3:
        pygame.draw.rect(window, bitter, box7)
        t1 = 'Process'

    if driver_State > 4:
        pygame.draw.rect(window, bitter, box8)
        t1 = 'Service'












