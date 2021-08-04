import pygame

clock = pygame.time.Clock()

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))

def getKey(KeyName):

    ans = False
    clock.tick(10)
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
	
    myKey = getattr(pygame, 'K_{}'.format(KeyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():

    if getKey('a'):
        print('Key a was pressed')
    if getKey('b'):
        print('Key b was pressed')


if __name__ == '__main__':
    init()
    while True:
        main()