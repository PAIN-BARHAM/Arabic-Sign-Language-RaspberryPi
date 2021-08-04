import pygame

clock = pygame.time.Clock()
# win = pygame.display.set_mode((100,100))
# define the RGB value
# for white colour
white = (255, 255, 255)

# assigning values to X and Y variable
X = 700
Y = 700

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption("Image")

# create a surface object, image is drawn on it.
image1 = pygame.image.load(r"/home/pi/Desktop/ArSL_proj/download.jpeg")
image2 = pygame.image.load(r"/home/pi/Desktop/ArSL_proj/Beh.jpeg")


def init():
    pygame.init()
    display_surface.fill(white)


def getKey(KeyName):

    ans = False
    clock.tick(10)
    for eve in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()

    myKey = getattr(pygame, "K_{}".format(KeyName))
    if keyInput[myKey]:
        ans = True

    pygame.display.update()

    return ans


def main():
    # completely fill the surface object
    # with white colour:

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.

    if getKey("a"):
        print("Key a was pressed")
        display_surface.fill(white)
        display_surface.blit(image1, (0, 0))
    if getKey("b"):
        print("Key b was pressed")
        display_surface.fill(white)
        display_surface.blit(image2, (0, 0))


if __name__ == "__main__":
    init()
    while True:
        main()
