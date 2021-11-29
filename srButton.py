import pygame

# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()    # img width
        height = image.get_height()  # img height
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))   # re-scale img based on scale provided
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False    # check if button was clicked or not

    def draw(self, surface):    # surface: where you wanna draw your button
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()    # mouse button

        # check mouseover and clicked conditions
        # [0] = LMB (Left Mouse Button)
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False    # When LMB is released reset it to false

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action               # If it was clicked return true so we can make decision based on the click

    def invertButton(normalImage, invertedImage, clicked, button):
        if clicked:
            button.image = invertedImage
        else:
            button.image = normalImage
