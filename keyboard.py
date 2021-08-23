import pygame
import cv2

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
import os
os.path.isfile('images/Alef.png') 


image1 = pygame.image.load(
    r"images/Alef.png"
)


image2 = pygame.image.load(
    r"images/Beh.png"
)

image3 = pygame.image.load(
    r"images/Wow.png"
)

image4 = pygame.image.load(
    r"images/Yeh.png"
)


def init():
    pygame.init()
    display_surface.fill(white)


def getKey(KeyName):

    ans = False
    pygame.time.delay(30)
    for eve in pygame.event.get():
        pass

    keyInput = pygame.key.get_pressed()

    myKey = getattr(pygame, "K_{}".format(KeyName))
    if keyInput[myKey]:
        ans = True

    pygame.display.update()

    return ans


Test = ""


def main():
    # completely fill the surface object
    # with white colour:

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    global Test

    if getKey("h"):
        print("Key a was pressed")
        display_surface.fill(white)
        # display_surface.blit(image1, (20, 20))
        Test += "h"

    if getKey("f"):
        print("Key b was pressed")
        display_surface.fill(white)
        display_surface.blit(image2, (20, 20))

    if getKey("d"):
        print("Key d was pressed")
        display_surface.fill(white)
        display_surface.blit(image4, (20, 20))

    if getKey("COMMA"):
        print("Key d was pressed")
        display_surface.fill(white)
        display_surface.blit(image3, (20, 20))

    if getKey("z"):
        print("Key z was pressed")
        display_surface.fill(white)
        pygame.display.quit()


    if getKey("e"):
        print("---------------------- Video .....................................")
        cap = cv2.VideoCapture('test.mp4')
        success, img = cap.read()
        shape = img.shape[1::-1]

        wn = pygame.display.set_mode(shape)
        clock = pygame.time.Clock()

        while success:
            clock.tick(60)
            success, img = cap.read()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    success = False
            wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
            pygame.display.update()


    if getKey("KP_ENTER"):
        display_surface.fill(white)
        print(Test)
        if Test == "h":
            display_surface.blit(image1, (20, 20))

        Test = ""


if __name__ == "__main__":
    init()
    print(pygame.display.Info())
    while True:
        main()
