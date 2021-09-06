#! /home/pi/.virtualenvs/sbb_cv/bin/python3
import pygame
import cv2

clock = pygame.time.Clock()
# win = pygame.display.set_mode((100,100))
# define the RGB value
# for white colour
white = (255, 255, 255)
green = (100, 100, 100)



# create the display surface object
# of specific dimension..e(X, Y).
# flags = pygame.FULLSCREEN

# assigning values to X and Y variable
X = 480
Y = 320

display_surface = pygame.display.set_mode((X, Y))

#screen_width = pygame.display.get_surface().get_size()[0]
#screen_height = pygame.display.get_surface().get_size()[1]

#width = screen_width // 2
#height = screen_height // 2


# set the pygame window name
pygame.display.set_caption("Image")

# create a surface object, image is drawn on it.
import os
os.path.isfile('images/Alef.png') 


Alef = pygame.image.load(
    r"images/Alef.png"
)


Baa = pygame.image.load(
    r"images/Baa.png"
)

Taa = pygame.image.load(
    r"images/Taa.png"
)

Jeem = pygame.image.load(
    r"images/Jeem.png"
)

Meem = pygame.image.load(
    r"images/Meem.png"
)

Daal = pygame.image.load(
    r"images/Daal.png"
)

Raa = pygame.image.load(
    r"images/Raa.png"
)

Seen = pygame.image.load(
    r"images/Seen.png"
)

Ta_marbuta = pygame.image.load(
    r"images/Ta_marbuta.png"
)
Yaa = pygame.image.load(
    r"images/Yaa.png"
)


def init():
    pygame.init()
    display_surface.fill(white)


def getKey(KeyName):

    ans = False
    pygame.time.delay(20)
    for eve in pygame.event.get():
        pass

    keyInput = pygame.key.get_pressed()

    myKey = getattr(pygame, "K_{}".format(KeyName))
    if keyInput[myKey]:
        ans = True

    pygame.display.update()

    return ans


Test = ""

def rescale_frame(frame, percent=50):
    width  = int(frame.shape[1] * percent/100)
    height = int(frame.shape[0] * percent/100)
    dim = (width,height)
    print(dim)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)


def rescale_image(image,percent):
    width = int(image.get_width() * percent/100)
    height = int(image.get_height() * percent/100)
    dim = (width, height)
    return pygame.transform.scale(image,dim)


def main():
    # completely fill the surface object
    # with white colour:

    global Test

    if getKey("BACKSPACE"):
        print("Key BACKSPACE was pressed")
        display_surface.fill(white)
        Test = ""

    if getKey("h"):
        print("Key a was pressed")
        display_surface.fill(white)
        image = rescale_image(Alef,90)
        display_surface.blit(image, (0,0))
        Test += "h"


    if getKey("f"):
        print("Key b was pressed")
        display_surface.fill(white)
        image = rescale_image(Baa,90)
        display_surface.blit(image, (0,0))
        Test += 'f'
        
    if getKey("j"):
        print("Key j was pressed")
        display_surface.fill(white)
        image = rescale_image(Taa,90)
        display_surface.blit(image, (0,0))
        Test += 'j'  
    

    if getKey("l"):
        print("Key l was pressed")
        display_surface.fill(white)
        image = rescale_image(Meem,90)
        display_surface.blit(image, (0,0))
        Test += "l"

    if getKey("v"):
        print("Key v was pressed")
        display_surface.fill(white)
        image = rescale_image(Raa,90)
        display_surface.blit(image, (0,0))
        Test += "v"

    if getKey("s"):
        print("Key s was pressed")
        display_surface.fill(white)
        image = rescale_image(Seen,90)
        display_surface.blit(image, (0, 0))
        Test += "S"

    if getKey("m"):
        print("Key m was pressed")
        display_surface.fill(white)
        image = rescale_image(Ta_marbuta,90)
        display_surface.blit(image, (0, 0))
        Test += "m"

    if getKey("RIGHTBRACKET"):
        print("Key ] was pressed")
        display_surface.fill(white)
        image = rescale_image(Daal,90)
        display_surface.blit(image, (0, 0))
        Test += "]"

    if getKey("d"):
        print("Key d was pressed")
        display_surface.fill(white)
        image = rescale_image(Yaa,90)
        display_surface.blit(image, (20, 20))
        Test += 'd'

    if getKey("ESCAPE"):
        print("Key z was pressed")
        display_surface.fill(white)
        pygame.display.quit()


    if getKey("e"):
        print("---------------------- Video .....................................")

        cap = cv2.VideoCapture('test.mp4')

        success, img = cap.read()
        shape = (448,252)
        print(shape)
        wn = pygame.display.set_mode(shape)
        clock = pygame.time.Clock()

        while success:
            clock.tick(60)
            success, img = cap.read()
            if img is not None:
                img = rescale_frame(img, percent=70)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    success = False
            if success:
                wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
                pygame.display.update()


    if getKey("RETURN"):
        print("RETURN BUTTON")
        display_surface.fill(white)
        
        if Test == "l]vSm":
            cap = cv2.VideoCapture('1.mp4')
            success, img = cap.read()
            shape = (448,246)
            wn = pygame.display.set_mode(shape)
            clock = pygame.time.Clock()

            while success:
                clock.tick(30)
                success, img = cap.read()
                if img is not None:
                    img = rescale_frame(img, percent=70)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        success = False
                if success:
                    wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
                    pygame.display.update()
        
        elif Test == "fdj":
            cap = cv2.VideoCapture('2.mp4')
            success, img = cap.read()
            shape = (448,246)
            wn = pygame.display.set_mode(shape)
            clock = pygame.time.Clock()

            while success:
                clock.tick(30)
                success, img = cap.read()
                if img is not None:
                    img = rescale_frame(img, percent=70)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        success = False
                        
                if success:
                    wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
                    pygame.display.update()    
                
        Test = ""


if __name__ == "__main__":
    init()
    print(pygame.display.Info())
    while True:
        main()