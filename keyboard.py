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


image1 = pygame.image.load(
    r"ArSL_Makanee/Images/Alef.jpg"
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
    pygame.time.delay(25)
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
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)


def rescale_image(image,percent):
    width = int(image.get_width() * percent/100)
    height = int(image.get_height() * percent/100)
    dim = (width, height)
    return pygame.transform.scale(image,dim)


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
        #shape = (448,252)
        #picture = pygame.transform.scale(image1,shape)
        picture = rescale_image(image1,10)
        display_surface.blit(picture, (0,0))
        Test += "h"

    if getKey("l"):
        print("Key l was pressed")
        display_surface.fill(white)
        # display_surface.blit(image1, (20, 20))
        Test += "l"

    if getKey("v"):
        print("Key v was pressed")
        display_surface.fill(white)
        # display_surface.blit(image1, (20, 20))
        Test += "v"

    if getKey("s"):
        print("Key s was pressed")
        display_surface.fill(white)
        # display_surface.blit(image1, (20, 20))
        Test += "S"

    if getKey("m"):
        print("Key m was pressed")
        display_surface.fill(white)
        # display_surface.blit(image1, (20, 20))
        Test += "m"

    if getKey("RIGHTBRACKET"):
        print("Key ] was pressed")
        display_surface.fill(white)
        # display_surface.blit(image1, (20, 20))
        Test += "]"

    if getKey("f"):
        print("Key b was pressed")
        display_surface.fill(white)
        shape = (448,252)
        picture = pygame.transform.scale(image2,shape)
        display_surface.blit(picture, (0,0))
        #display_surface.blit(image2, (20, 20))

    if getKey("d"):
        print("Key d was pressed")
        display_surface.fill(white)
        display_surface.blit(image4, (20, 20))

    if getKey("COMMA"):
        print("Key d was pressed")
        
        display_surface.fill(white)
        display_surface.blit(image3, (20, 20))

    if getKey("ESCAPE"):
        print("Key z was pressed")
        display_surface.fill(white)
        pygame.display.quit()


    if getKey("e"):
        print("---------------------- Video .....................................")

        cap = cv2.VideoCapture('test.mp4')
        #cap.set(3,480)
        #cap.set(4,320)
        #cap.resize(189)
        success, img = cap.read()
        #img = rescale_frame(img, percent=50)
        #shape = img.shape[1::-1]
        #shape = (640,180)
        shape = (448,252)
        print(shape)
        wn = pygame.display.set_mode(shape)
        clock = pygame.time.Clock()

        while success:
            clock.tick(60)
            success, img = cap.read()
            #if not isinstance(img, NoneType):
            if img is not None:
                img = rescale_frame(img, percent=70)
            #print("After_scaling: {}".format(img.shape[1::-1]))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    success = False
            if success:
                wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
                pygame.display.update()
        #display_surface.fill(white)


    if getKey("RETURN"):
        print("RETURN BUTTON")
        display_surface.fill(white)
        print(Test)
        if Test == "h":
            display_surface.blit(image1, (20, 20))
        
        if Test == "l]vSm":
            cap = cv2.VideoCapture('1.mp4')
            success, img = cap.read()
            shape = img.shape[1::-1]

            wn = pygame.display.set_mode(shape)
            clock = pygame.time.Clock()

            while success:
                clock.tick(30)
                success, img = cap.read()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        success = False
                if success:
                    wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
                    pygame.display.update()
                
                #print("Hello World")

        Test = ""
    
    # if getKey('RETURN'):
    #     print("KP_RETURN")


if __name__ == "__main__":
    init()
    print(pygame.display.Info())
    while True:
        main()




