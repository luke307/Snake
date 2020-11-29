import pygame


pygame.display.init()

sets = { #settings
    'FPS' : 60,
    'width' : 600,
    'height' : 600
}

col = { #colour
    'black' : (0,0,0),
    'red'   : (255,0,0),
    'white' : (255,255,255)
}


def main():

    screen = pygame.display.set_mode((sets['width'],sets['height']))
    clock = pygame.time.Clock()
    x=1
    y=1
    running = True

    while running:

        clock.tick(sets['FPS'])

        screen.fill(col['white'])

        pygame.draw.rect(screen, col['black'] , [x, y, 10, 10])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RIGHT:
                     x+=2
                 elif event.key == pygame.K_LEFT:
                     x-=2
                 elif event.key == pygame.K_DOWN:
                     y+=2    
                 elif event.key == pygame.K_UP:
                     y-=2        

        pygame.display.update()


main()
