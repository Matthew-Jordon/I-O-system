import pygame



#Button Texts
t1 = 'Next'



DMA_State = 0



#Colours used for DMA
bg_colour = (0, 48, 73)
colour1 = (234, 226, 183)
orange = (252, 191, 73)
outline_colour = orange
WHITE = (255,255,255)
BLACK = (0,0,0)
Maxim_Red = (214, 40, 40)
pipe = (247, 127, 0)
magenta = (255,0,255)





def clean(window,label): # Clear prev state, get things set up
    window.fill(bg_colour) # bg colour
    DMA_title = label.render('DMA', 1, WHITE)  # Make label for title
    window.blit(DMA_title, (340, 40))  # show DMA_title label at relevant spot


def initial_DMA(window, label):

    outline =  pygame.Rect(400, 220, 300, 340)
    pygame.draw.rect(window, outline_colour, outline)

    filler_bg =  pygame.Rect(420, 240, 260, 300)
    pygame.draw.rect(window, bg_colour, filler_bg)

    box1 = pygame.Rect(150, 250, 200, 100)
    box2 = pygame.Rect(450, 250, 200, 100)
    box3 = pygame.Rect(450, 420, 200, 100)

    pygame.draw.rect(window, colour1, box1)
    pygame.draw.rect(window, colour1, box2)
    pygame.draw.rect(window, colour1, box3)

    t1 = label.render('CPU', 1, BLACK)  # Make label for title
    window.blit(t1, (230, 290))  # show DMA_title label at relevant spot
    t2 = label.render('I/O', 1, BLACK)  # Make label for title
    window.blit(t2, (540, 290))  # show DMA_title label at relevant spot
    t3 = label.render('Memory', 1, BLACK)  # Make label for title
    window.blit(t3, (525, 460))  # show DMA_title label at relevant spot



    #make_connections(window)

    #show_dma(window)


def make_connections(window):

    #pipes = the orange connectors that are made to show connection between boxes

    pipe1 = pygame.Rect(350, 290, 100, 10)
    pipe2 = pygame.Rect(250, 350, 10, 120)
    pipe3 = pygame.Rect(250, 460, 200, 10)


    pygame.draw.rect(window, pipe, pipe1)
    pygame.draw.rect(window, pipe, pipe2)
    pygame.draw.rect(window, pipe, pipe3)

    font = pygame.font.SysFont('arial', 15)

    t1 = font.render('Cycle 1', 1, WHITE)  # Make label for title
    window.blit(t1, (355, 300))  # show label at relevant spot
    t2 = font.render('Cycle 2', 1, WHITE)  # Make label for title
    window.blit(t2, (250, 480))  # show label at relevant spot


def show_dma(window): # show dma, that we can reduce 1 cycle if we directly hook up memory and io

    global  outline_colour
    outline_colour = Maxim_Red

    pipe1 = pygame.Rect(540, 350, 10, 70)
    pygame.draw.rect(window, Maxim_Red, pipe1)

    font = pygame.font.SysFont('arial', 15)

    t1 = font.render('Only 1 Cycle', 1, WHITE)  # Make label for title
    window.blit(t1, (560, 360))  # show label at relevant spot
    t2 = font.render('If directly Connected', 1, WHITE)  # Make label for title
    window.blit(t2, (560, 390))  # show label at relevant spot



def show_main_diag(window,title,font):


    clean(window,title) # wipe prev diags & reset everything

    box1 = pygame.Rect(50, 200, 100, 300)
    box2 = pygame.Rect(240, 200, 100, 300)
    box3 = pygame.Rect(450, 200, 100, 300)
    box4 = pygame.Rect(650, 200, 102, 300)

    pygame.draw.rect(window, colour1, box1)
    pygame.draw.rect(window, colour1, box2)
    pygame.draw.rect(window, colour1, box3)
    pygame.draw.rect(window, colour1, box4)


    t1 = font.render('CPU', 1, BLACK)  # Make label for title
    window.blit(t1, (80, 300))  # show label at relevant spot
    t2 = font.render('DMAC', 1, BLACK)  # Make label for title
    window.blit(t2, (265, 300))  # show label at relevant spot
    t3 = font.render('Buffer', 1, BLACK)  # Make label for title
    window.blit(t3, (475, 300))  # show label at relevant spot
    t4 = font.render('Main Memory', 1, BLACK)  # Make label for title
    window.blit(t4, (651, 300))  # show label at relevant spot

    pipe1 = pygame.Rect(95, 500, 10, 30)
    pipe2 = pygame.Rect(285, 500, 10, 30)
    pipe3 = pygame.Rect(495, 500, 10, 30)
    pipe4 = pygame.Rect(695, 500, 10, 30)

    pygame.draw.rect(window, magenta, pipe1)
    pygame.draw.rect(window, magenta, pipe2)
    pygame.draw.rect(window, magenta, pipe3)
    pygame.draw.rect(window, magenta, pipe4)

    pipe1A = pygame.Rect(95, 530, 190, 10)
    pipe2A = pygame.Rect(285, 530, 210, 10)
    pipe3A = pygame.Rect(495, 530, 210, 10)
    pipe4A = pygame.Rect(95, 550, 610, 10)
    pipe5A = pygame.Rect(95, 540, 10, 10)
    pipe6A = pygame.Rect(695, 540, 10, 10)

    pygame.draw.rect(window, magenta, pipe1A)
    pygame.draw.rect(window, magenta, pipe2A)
    pygame.draw.rect(window, magenta, pipe3A)
    pygame.draw.rect(window, magenta, pipe4A)
    pygame.draw.rect(window, magenta, pipe5A)
    pygame.draw.rect(window, magenta, pipe6A)

    t5 = font.render('Bus', 1, magenta)  # Make label for title
    window.blit(t5, (375, 560))  # show label at relevant spot




#show forward connections and access indices
def label_1(window, font, small_font):

    pipe1B = pygame.Rect(150, 310, 90, 10)
    pipe2B = pygame.Rect(340, 310, 110, 10)
    pipe4B = pygame.Rect(550, 310, 100, 10)

    pygame.draw.rect(window, Maxim_Red, pipe1B)
    pygame.draw.rect(window, Maxim_Red, pipe2B)
    pygame.draw.rect(window, Maxim_Red, pipe4B)

    t6 = font.render('1', 1, WHITE)  # Make label for title
    window.blit(t6, (195, 285))  # show label at relevant spot
    t7 = font.render('2', 1, WHITE)  # Make label for title
    window.blit(t7, (385, 285))  # show label at relevant spot
    t8 = font.render('3', 1, WHITE)  # Make label for title
    window.blit(t8, (595, 285))  # show label at relevant spot

    t12 = small_font.render('Program DMAC', 1, WHITE)  # Make label for title
    window.blit(t12, (155, 265))  # show label at relevant spot
    t13 = small_font.render('Store data', 1, WHITE)  # Make label for title
    window.blit(t13, (345, 265))  # show label at relevant spot
    t14 = small_font.render('Transfer data', 1, WHITE)  # Make label for title
    window.blit(t14, (555, 265))  # show label at relevant spot






#show backward connections and access indices
def label_2(window,font, small_font):
    pipe3B = pygame.Rect(150, 330, 90, 10)
    pipe5B = pygame.Rect(340, 330, 110, 10)
    pipe6B = pygame.Rect(550, 330, 100, 10)

    pygame.draw.rect(window, Maxim_Red, pipe3B)
    pygame.draw.rect(window, Maxim_Red, pipe5B)
    pygame.draw.rect(window, Maxim_Red, pipe6B)

    t9 = font.render('4', 1, WHITE)  # Make label for title
    window.blit(t9, (595,345))  # show label at relevant spot
    t10 = font.render('5', 1, WHITE)  # Make label for title
    window.blit(t10, (385, 345))  # show label at relevant spot
    t11 = font.render('6', 1, WHITE)  # Make label for title
    window.blit(t11, (195, 345))  # show label at relevant spot

    t12 = small_font.render('Interrupt when done', 1, WHITE)  # Make label for title
    window.blit(t12, (155, 375))  # show label at relevant spot
    t13 = small_font.render('Acknowledge', 1, WHITE)  # Make label for title
    window.blit(t13, (345, 375))  # show label at relevant spot
