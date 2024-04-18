import pygame
pygame.init()

pygame.display.set_caption("running Game")
bird_movement = 45
velocity_x = 0
init_velocity = 5
screen_width = 1000
screen_height = 400
DEFAULT_IMAGE_SIZE=(1000,400)
FLOOR_SIZE=(1000,400)
clock=pygame.time.Clock()
fps=60


gameWindow = pygame.display.set_mode((screen_width, screen_height))

bird_downflap = pygame.image.load('flappy_bird/sprites/bluebird-downflap.png').convert()
bg_surface = pygame.image.load('flappy_bird/sprites/background-night.png').convert()
floor_surface = pygame.image.load('flappy_bird/sprites/base.png').convert()
bg_surface = pygame.transform.scale(bg_surface, DEFAULT_IMAGE_SIZE)
floor_surface=pygame.transform.scale(floor_surface,FLOOR_SIZE)


exit_game = False
game_over = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("lefyt")
                velocity_x = init_velocity
                velocity_y = 0
            bird_movement = bird_movement + velocity_x
        gameWindow.blit(bg_surface, (0, 0))
        gameWindow.blit(floor_surface, (0, 300))
        gameWindow.blit(bird_movement,(0,300))
        pygame.display.update()
        clock.tick(fps)

pygame.quit()
quit()