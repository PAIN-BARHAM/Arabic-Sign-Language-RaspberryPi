import pygame,time

def aspect_scale(img,bx,by):
    """ Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    ix,iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx/float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by/float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx/float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by
    return pygame.transform.scale(img, (int(sx),int(sy)))

def imgToScrn(scrn,imgFilename):
    img = pygame.image.load(imgFilename)

    scaledImg = aspect_scale(img,scrnRect[scrn].width,scrnRect[scrn].height)
    siRect = scaledImg.get_rect()
    siRect.center = scrnRect[scrn].center

    screen.blit(scaledImg, siRect)
    pygame.display.flip()


scrnRect = [pygame.Rect(0,0,800,480),
            pygame.Rect(0,0,800,480)]

pygame.init()
displayInfo = pygame.display.Info()
print(displayInfo)

displayWidth = displayInfo.current_w
displayHeight = displayInfo.current_h

screen = pygame.display.set_mode((displayWidth,displayHeight),pygame.FULLSCREEN)
#screen.fill(pygame.Color('black'))

imgToScrn(0,'/home/pi/Desktop/ArSL_proj/download.jpeg')
time.sleep(2)

imgToScrn(1,'/home/pi/Desktop/ArSL_proj/Beh.jpeg')
time.sleep(2)

pygame.quit()
quit()