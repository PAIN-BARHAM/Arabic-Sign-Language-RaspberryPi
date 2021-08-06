import pygame

clock = pygame.time.Clock()
# win = pygame.display.set_mode((100,100))
# define the RGB value
# for white colour
white = (255, 255, 255)
green = (100, 100, 100)

# assigning values to X and Y variable
X = 0

Y = 0

# create the display surface object
# of specific dimension..e(X, Y).
flags = pygame.FULLSCREEN
display_surface = pygame.display.set_mode((X, Y))

screen_width = pygame.display.get_surface().get_size()[0]
screen_height = pygame.display.get_surface().get_size()[1]

width = screen_width // 2
height = screen_height // 2


# set the pygame window name
pygame.display.set_caption("Image")

# create a surface object, image is drawn on it.
image1 = pygame.image.load(r"/home/pi/Desktop/ArSL_proj/Alef.png")
image1 = pygame.transform.scale(image1, (400, 240))

image2 = pygame.image.load(r"/home/pi/Desktop/ArSL_proj/Beh.png")
image2 = pygame.transform.scale(image2, (400, 240))


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
        display_surface.blit(image1, (20, 20))
    if getKey("b"):
        print("Key b was pressed")
        display_surface.fill(white)
        display_surface.blit(image2, (20, 20))

    if getKey("z"):
        print("Key z was pressed")
        display_surface.fill(white)
        pygame.display.quit()


if __name__ == "__main__":
    init()
    print(pygame.display.Info())
    while True:
        main()
