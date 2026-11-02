import pygame

screen_width = 800
screen_height = 600
remaining_time = 60  # in seconds
running = True
player=pygame.Rect(50, 320, 50, 50)  # Player's rectangle (x, y, width, height)
pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sliding Through the Hood")
clock = pygame.time.Clock()
jump_duration = 200  # Duration of the jump in milliseconds
jump_happened = False  # Flag to track if the jump has occurred
jump_start_time = 0  # Variable to store the start time of the jump
def draw_sky():
    image = pygame.image.load("rajvosa.jpg")  # Load the background image
    window.fill((0, 0, 0))  # Fill the window with black color
    window.blit(image)  # Draw the background image
def draw_rect():
    rect_width = 800
    rect_height = 230
    rect_x = 0
    rect_y = 600 - rect_height  # Position the rectangle at the bottom of the window
    pygame.draw.rect(window, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))
def draw_object():
    pygame.draw.rect(window, "blue", (player.x, player.y, player.width, player.height))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
            if event.key == pygame.K_UP:
                player.y -= 10  # Move the player up
            elif event.key == pygame.K_DOWN:
                player.y += 10  # Move the player down
            elif event.key == pygame.K_RIGHT: 
                player.x += 10  # Move the player right
            elif event.key == pygame.K_LEFT:
                player.x -= 10  # Move the player left
            elif event.key == pygame.K_SPACE and not jump_happened:  # Check if the space key is pressed and jump hasn't happened yet
                jump_happened = True
                jump_start_time = pygame.time.get_ticks()
                player.y = max(player.y - 50, 0)
                
    if jump_happened and pygame.time.get_ticks() - jump_start_time >= jump_duration:
        player.y += 50
        jump_happened = False
    draw_sky()
    draw_rect()
    draw_object()
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS