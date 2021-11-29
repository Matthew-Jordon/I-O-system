import pygame




#Colours used for deviceDriverAndController
bg_colour = (0, 109, 119)
colour1 = (253, 252, 220)
orange = (252, 191, 73)
outline_colour = orange
WHITE = (255,255,255)
BLACK = (0,0,0)
Maxim_Red = (214, 40, 40)
pipe = (247, 127, 0)
magenta = (255,0,255)
peach = (254, 217, 183)
teal = (131, 197, 190)
silk = (226, 149, 120)
int_colour = colour1


example_state = 0
t1 = 'Send Input'


def clean(window,label,box_label,small_label): # Clear prev state, get things set up
    window.fill(bg_colour) # bg colour
    DMA_title = label.render('Example', 1, WHITE)  # Make label for title
    window.blit(DMA_title, (310, 40))  # show DMA_title label at relevant spot

    initial_Structure(window, box_label, small_label)


def initial_Structure(window, label, small):
    box1 = pygame.Rect(25, 350, 150, 100)
    box2 = pygame.Rect(200, 350, 150, 100)
    box3 = pygame.Rect(450, 350, 150, 100)
    box4 = pygame.Rect(640, 250, 100, 300)
    box5 = pygame.Rect(440, 340, 170, 120)
    box6 = pygame.Rect(365, 250, 60, 300)



    pygame.draw.rect(window, peach, box5)
    pygame.draw.rect(window, colour1, box1)
    pygame.draw.rect(window, colour1, box2)
    pygame.draw.rect(window, colour1, box3)
    pygame.draw.rect(window, colour1, box4)
    pygame.draw.rect(window, int_colour, box6)


    t2 = label.render('Device', 1, BLACK)  # Make label for title
    window.blit(t2, (80, 390))  # show device label at relevant spot
    t3 = label.render('Device Controller', 1, BLACK)  # Make label for title
    window.blit(t3, (210, 390))  # show controller label at relevant spot
    t4 = label.render('Device Driver', 1, BLACK)  # Make label for title
    window.blit(t4, (475, 390))  # show driver label at relevant spot
    t5 = label.render('OS', 1, BLACK)  # Make label for title
    window.blit(t5, (680, 390))  # show OS label at relevant spot
    t6 = small.render('I/O System', 1, BLACK)  # Make label for title
    window.blit(t6, (500, 338))  # show OS label at relevant spot

    t7 = small.render('Interrupt', 1, BLACK)  # Make label for title
    window.blit(t7, (377, 390))  # show OS label at relevant spot

    draw_connections(window)

def draw_connections(window):

    global t1
    global int_colour

    box6 = pygame.Rect(175, 400, 25, 10)
    box7 = pygame.Rect(350, 400, 15, 10)
    box8 = pygame.Rect(425, 400, 15, 10)
    box9 = pygame.Rect(610, 400, 30, 10)

    if example_state > 2:
        pygame.draw.rect(window, silk, box6)

    if example_state > 3:
        pygame.draw.rect(window, silk, box7)


        t1 = 'Receive input'

    if example_state > 4:
        pygame.draw.rect(window, silk, box8)
        int_colour = teal
        t1 = 'Send Interrupt'

    if example_state > 5:
        pygame.draw.rect(window, silk, box9)
        t1 = 'Serve Request'


    if example_state > 6:
        int_colour = colour1
        t1 = 'Served Request'
