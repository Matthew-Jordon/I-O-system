import pygame

# Constants used globally and for interrupts, they are here so the main game file doesnt get cluttered


#Base constants to get the game running

window_size = (800,800) # screen size
run = True              # if false, the game ends

capt_text = 'I/O Systems' # The title_interrupt of the window of the game

clock = pygame.time.Clock() # clock to set FPS to desired fps, we set it to 60, so it doesnt overload the system running it






# titles for interrupts screen

interrupts_bg_colour = (23, 54, 87)
title_interrupt = "Interrupts"
t1 = "Process Executing"
t2 = "Create Interrupt"
t3 = "Interrupt"
t4 = "Save Context"
t5 = "Interrupt Handler"
t6 = "Processing"
t7 = "Restore Context"
