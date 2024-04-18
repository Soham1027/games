import pygame

x = pygame.init()
# create window
white = (255, 255, 255)
x = 1200
y = 500

screen = pygame.display.set_mode((x, y))
# Game variable
exit_game = False
game_over = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")

            elif event.key == pygame.K_LEFT:
                print("You have pressed left arrow key")

            elif event.key == pygame.K_UP:
                print("You have pressed up arrow key")

            elif event.key == pygame.K_DOWN:
                print("You have pressed down arrow key")

            elif event.key == pygame.K_SPACE:
                print("You have pressed space bar key")

            elif event.key == pygame.K_w:
                print("You have pressed w for up")

            elif event.key == pygame.K_a:
                print("You have pressed a for left")
            elif event.key == pygame.K_s:
                print("You have pressed s for down")
            elif event.key == pygame.K_d:
                print("You have pressed a for right")


pygame.quit()
quit()
