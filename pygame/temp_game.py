import random

import pygame

# import random

pygame.init()

# images & Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
pygame.display.set_caption("Flappy Game")
screen_width = 400
screen_height = 700
gameWindow = pygame.display.set_mode((screen_width, screen_height))

bg_surface = pygame.image.load('flappy_bird/sprites/background-night.png').convert()
floor_surface = pygame.image.load('flappy_bird/sprites/base.png').convert()

bird_downflap = pygame.image.load('flappy_bird/sprites/bluebird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('flappy_bird/sprites/bluebird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('flappy_bird/sprites/bluebird-upflap.png').convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_react = bird_surface.get_rect(center=(100, 350))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# bird_surface = pygame.image.load('flappy_bird/sprites/bluebird-midflap.png').convert_alpha()
# bird_react = bird_surface.get_rect(center=(100, 350))
pipe_surface = pygame.image.load('flappy_bird/sprites/pipe-red.png')

DEFAULT_IMAGE_SIZE = (400, 700)
FLOOR_SIZE = (400, 100)
PIPE_SIZE = (0, 600)
floor_x_pos = 0
bg_surface = pygame.transform.scale(bg_surface, DEFAULT_IMAGE_SIZE)
floor_surface = pygame.transform.scale(floor_surface, FLOOR_SIZE)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)
pipe_height = [350, 400, 500]

# variables
gravity = .25
bird_movement = 0
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19__.TTF', 40)
fps = 50
score = 0
high_score = 0
exit_game = False
game_over = False
game_active = True


# gameloop
def draw_floor():
    gameWindow.blit(floor_surface, (floor_x_pos, 600))
    gameWindow.blit(floor_surface, (floor_x_pos + 400, 600))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(450, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(450, random_pipe_pos - 300))

    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return pipes


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, bird_movement * 3, 1)
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_react = new_bird.get_rect(center=(100, bird_react.centery))
    return new_bird, new_bird_react


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            gameWindow.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            gameWindow.blit(flip_pipe, pipe)

    return pipes


def check_collision(pipes):
    for pipe in pipes:
        if bird_react.colliderect(pipe):
            return False

    if bird_react.top <= -150 or bird_react.bottom >= 900:
        return False
    return True


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_react = score_surface.get_rect(center=(200, 100))
        gameWindow.blit(score_surface, score_react)
    if game_state == "game_end":
        score_surface = game_font.render(f'Score:{int(score)}', True, (255, 255, 255))
        score_react = score_surface.get_rect(center=(200, 100))
        gameWindow.blit(score_surface, score_react)

        high_score_surface = game_font.render(f'High Score:{int(high_score)}', True, (255, 255, 255))
        high_score_react = score_surface.get_rect(center=(150, 550))
        gameWindow.blit(high_score_surface, high_score_react)


while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement -= 7
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_react.center = (100, 350)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird_surface, bird_react = bird_animation()

    # bird
    gameWindow.blit(bg_surface, (0, 0))
    if game_active:
        bird_movement += gravity
        bird_rotate = rotate_bird(bird_surface)
        bird_react.centery += bird_movement
        gameWindow.blit(bird_rotate, bird_react)
        game_active = check_collision(pipe_list)

        # pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score += 0.01
        score_display('main_game')
    else:
        high_score = update_score(score, high_score)
        score_display('game_end')

    # floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -400:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(fps)
