# Programmer:
# Date:
# Description:

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Import functions for using sprites
from ucc_sprite import Sprite

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((640, 360))

# Set the title of the pygame screen
pygame.display.set_caption("Frogger")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.Group()

### SET UP YOUR GAME HERE

# Create a background surface
background = pygame.Surface((640, 360))
background.fill("aquamarine")

# Load the images
frog_image = pygame.image.load("frog.png")

# Create the sprites
frogger = Sprite(frog_image)
frogger.direction = 90
frogger.rotates = False
frogger.center = (320,180)
frogger.add(all_sprites)

# Add the background image
screen.fill("aquamarine")

# Main Loop
while True:
    # Set the frame rate to 30 frames per second
    clock.tick(30)

    ### MANAGE IN-GAME EVENTS AND ANIMATIONS HERE

    # Clear the old images of the sprites from the screen
    all_sprites.clear(screen, background)

    # Update the sprites' locations
    all_sprites.update()

    # Redraw the sprites
    all_sprites.draw(screen)

    # Flip the changes to the screen to the computer display
    pygame.display.flip()
