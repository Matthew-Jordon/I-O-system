import pygame
import constants #import global constants
import srButton  #import button maker class (file)
import DMA
import deviceDriverAndController
import example

pygame.init() #To get things started

window = pygame.display.set_mode(constants.window_size) # setting the window size to WxH and making the screen we see

pygame.display.set_caption(constants.capt_text) # setting the caption we see on the top bar

start_img = pygame.image.load('plain square.png').convert_alpha() # creating the image for the button that we place at the bottom

# create button instances
start_button = srButton.Button(250,630, start_img, 1)
# Title
# Different titles and fonts used for different areas
title_font = pygame.font.SysFont('arial', 50)
box_font = pygame.font.SysFont('arial', 20)
small_font = pygame.font.SysFont('arial', 12)
start_button_font = pygame.font.SysFont('arial', 25)

interrupt_state = 0 # we use this to detect which state the game currently is in. We use this to decide what we need to show / hide on the screen
start_X = 320 # X-coordinate position of the button font

# Boxes we make and show on the window, they are global so we can maintain their state and change their properties at will
process = pygame.Rect(50,200,150,100)
executing_sim = pygame.Rect(50,270,10,10)
btn = pygame.Rect(200,600,100,300)


# Colours needed throughout the code, Colour = ( R, G, B ). These are RAW static values
WHITE = (255, 255, 255)
TEAL = (54, 117, 136)
RED = (240, 0, 0)
YELLOW = (228, 208, 10)
GREY = (96, 96, 96)
BLACK = (0, 0, 0)
ORANGE = (255,140,0)
GREEN = (50, 205, 50)
Dark_Yellow = (155,135,12)
Dark_Grey = (51, 51, 51)

# Colours assigned to the boxes, they are global so we can change them later on to other colours. Variable values
executing_sim_Colour= RED
process_Colour = TEAL
context_Colour = ORANGE
colourProcessed = WHITE
interruptBoxColour = YELLOW
restoreColour = Dark_Grey


# Constants needed for interrupt view
goRight = True # To decide if the red square moves <- & ->
makeProgressBar = False # To decide if we need to keep making the progress bar (green). If false, the computer seizes to make that bar
loaderView = pygame.Rect(250, 420, 10, 10) # For the progress bar, we assign an inital X, Y, Width, Height. We keep increasing the W so it 'looks' like the bar is doing work





# Box
# We make rectangles (Boxes) by this box = pygame.Rect(X, Y, Width, Height). We provide the X,Y coordinates and then the height and width. All boxes are made with this code
# Then to make the box we created visible onto the screen, we use  pygame.draw.rect(window,colour,box). If we dont do this we will never see the box, i.e. it doesnt get printed
# onto the screen



#                                                           Interrupt Work *START*

# Interrupt scren functions. Depending on the interrupt_state, we choose the relevant func to fire.


def show_execution():
    global goRight # A var we use to decide what direction the square should move in ( like a toggle)


    if goRight:
        executing_sim[0] += 2 # We change the x pos of the square to make it appear like its moving for R.H.S we increment
        if executing_sim[0] > 190:
            goRight = False
    else:
        executing_sim[0] -= 2
        if executing_sim[0] < 52: # For L.H.S we decrement
            goRight = True


def show_interrupt():
    interruptBox = pygame.Rect(50, 350, 150, 80)
    pygame.draw.rect(window,interruptBoxColour,interruptBox)
    text = box_font.render(constants.t3, 1, WHITE)  # Make label for box 1
    window.blit(text, (95, 380))  # show title_interrupt label at relevant spot

    interruptLine = pygame.Rect(120, 300, 10, 50)
    pygame.draw.rect(window,BLACK,interruptLine)

    global process_Colour
    global executing_sim_Colour

    executing_sim_Colour = YELLOW
    process_Colour = GREY

    constants.t1 = 'Process Paused'
    constants.t2 = 'Handle Interrupt'


def handle_interrupt():
    saveContext = pygame.Rect(250, 200, 150, 100)
    pygame.draw.rect(window, context_Colour, saveContext)
    text = box_font.render(constants.t4, 1, WHITE)  # Make label for box 1
    window.blit(text, (275, 240))  # show title_interrupt label at relevant spot

    contextLine = pygame.Rect(200, 250, 50, 10)
    pygame.draw.rect(window,BLACK,contextLine)


def interrupt_handler():
    constants.t2 = 'Working On Interrupt'
    global start_X
    start_X = 290

    global  colourProcessed

    global  makeProgressBar
    makeProgressBar = True

    global context_Colour
    context_Colour = GREEN
    constants.t4 = 'Saved Context'

    intHandler = pygame.Rect(250, 350, 150, 80)
    pygame.draw.rect(window, GREY, intHandler)
    text = box_font.render(constants.t5, 1, WHITE)  # Make label for box 1
    window.blit(text, (265, 360))  # show title_interrupt label at relevant spot
    text2 = box_font.render(constants.t6, 1, colourProcessed)  # Make label for box 1
    window.blit(text2, (285, 390))  # show title_interrupt label at relevant spot

    intLine = pygame.Rect(320, 300, 10, 50)
    pygame.draw.rect(window, BLACK, intLine)

    global loaderView
    pygame.draw.rect(window, GREEN, loaderView)

    #simulate loading bar
    if makeProgressBar and loaderView.width<150:
        loaderView.width+=1.5

    if loaderView.width >= 150:
        makeProgressBar = False
        constants.t6 = 'Processed'
        colourProcessed = GREEN


def resume_context():
    global start_X
    start_X = 315
    constants.t2 = 'Restore Context'

    resume = pygame.Rect(450, 350, 150, 80)
    pygame.draw.rect(window, restoreColour, resume)
    text = box_font.render(constants.t7, 1, WHITE)  # Make label for box 1
    window.blit(text, (460, 360))  # show title_interrupt label at relevant spot


def resume_prev_work():

    constants.t2 = 'Go to Previous Work'
    constants.t7 = 'Restored Context'

    global restoreColour
    restoreColour = GREY

    global start_X

    start_X = 300

    bar = pygame.Rect(400, 390, 50, 10)
    pygame.draw.rect(window, BLACK, bar)

    bar_1= pygame.Rect(400, 250, 120, 7)
    pygame.draw.rect(window, YELLOW, bar_1)

    bar_2= pygame.Rect(520, 250, 7, 100)
    pygame.draw.rect(window, YELLOW, bar_2)


def resume():

    constants.t1 = 'Process Executing'
    global interruptBoxColour
    global executing_sim_Colour
    global process_Colour
    executing_sim_Colour = RED
    process_Colour = TEAL
    interruptBoxColour = Dark_Yellow

#                                                            Interrupt Work *END*







while constants.run: # The main game loop. All processing happens here with the functions we defined above


    window.fill(constants.interrupts_bg_colour) # Set bg colour of screen 1

    pygame.draw.rect(window,process_Colour,process)
    pygame.draw.rect(window,executing_sim_Colour,executing_sim)



    b1 = box_font.render(constants.t1, 1, WHITE)  # Make label for box 1
    window.blit(b1, (55, 210))  # show title_interrupt label at relevant spot

    # Interrutps

    if interrupt_state == 0 or interrupt_state > 5:
        show_execution()
    if interrupt_state > 0:
        show_interrupt()

    if interrupt_state > 1:
        handle_interrupt()

    if interrupt_state > 2:
        interrupt_handler()

    if interrupt_state > 3:
        resume_context()

    if interrupt_state > 4:
        resume_prev_work()

    if interrupt_state > 5:
        resume()

    # DMA

    if DMA.DMA_State >= 0 and interrupt_state > 6:
        DMA.clean(window, title_font)
        DMA.initial_DMA(window, box_font)

    if DMA.DMA_State == 2:
        DMA.make_connections(window)

    if DMA.DMA_State == 3:
        DMA.show_dma(window)

    if DMA.DMA_State >3:
        DMA.show_main_diag(window,title_font,box_font)

    if DMA.DMA_State > 4:
        DMA.label_1(window,box_font,small_font)

    if DMA.DMA_State > 5:
        DMA.label_2(window,box_font,small_font)


    # Device controller/driver

    if deviceDriverAndController.driver_State>=0 and DMA.DMA_State >6:
        deviceDriverAndController.clean(window,title_font,box_font,small_font)

    if deviceDriverAndController.driver_State > 0:
        deviceDriverAndController.draw_connections(window)


    # Example

    if example.example_state>=0 and deviceDriverAndController.driver_State > 5:
        example.clean(window,title_font,box_font,small_font)



    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                constants.run = False  # Kill the game on escape key
                print('\nShutting down the game')





        if event.type == pygame.QUIT:
            constants.run = False #Kill the game


    # Title of the Current Process [On top of the screen]
    if interrupt_state < 7:

        interrupt_title = title_font.render(constants.title_interrupt, 1, WHITE)  # Make label
        window.blit(interrupt_title, (300, 40))  # show title_interrupt label at relevant spot

    if start_button.draw(window):

        if interrupt_state <= 6:
            interrupt_state += 1
            #print('current Interrupt State = ', interrupt_state)

        if interrupt_state > 6:
            interrupt_state = 7

        if interrupt_state > 6:
            DMA.DMA_State += 1
            #print('current DMA State = ', DMA.DMA_State)

        if DMA.DMA_State > 5:
            deviceDriverAndController.driver_State+=1
            #print('current Device Driver & Controller State = ', deviceDriverAndController.driver_State)


        if example.example_state >= 0 and deviceDriverAndController.driver_State > 4:
            example.example_state+=1
            #print('current example State = ',  example.example_state)





    #  Button titles [The button at the bottom of the screen]

    #Interrupts
    if interrupt_state < 7:
        start_btn_font = start_button_font.render(constants.t2, 1, WHITE)  # Make label for box 1
        window.blit(start_btn_font, (start_X, 670))  # show title_interrupt label at relevant spot

    #DMA
    if interrupt_state > 6 and deviceDriverAndController.driver_State <= 0:
        start_btn_font = start_button_font.render(DMA.t1, 1, WHITE)  # Make label for box 1
        window.blit(start_btn_font, (370, 670))  # show title_interrupt label at relevant spot

    #Device Driver & Controller
    if DMA.DMA_State > 6 and deviceDriverAndController.driver_State <= 5:
        start_btn_font = start_button_font.render(deviceDriverAndController.t1, 1, WHITE)  # Make label for box 1
        window.blit(start_btn_font, (340, 670))  # show title_interrupt label at relevant spot

    if DMA.DMA_State == 6:
        start_btn_font = start_button_font.render('Next', 1, WHITE)  # Make label for box 1
        window.blit(start_btn_font, (370, 670))  # show title_interrupt label at relevant spot

    #Example
    if deviceDriverAndController.driver_State > 5:
        start_btn_font = start_button_font.render(example.t1, 1, WHITE)  # Make label for box 1
        start_X = 325
        window.blit(start_btn_font, (start_X, 670))  # show title_interrupt label at relevant spot



    pygame.display.update()
    constants.clock.tick(60)




pygame.quit()