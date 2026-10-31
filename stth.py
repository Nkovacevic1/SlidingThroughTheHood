import pygame

screen_width = 800
screen_height = 600
remaining_time = 60  # in seconds
running = True
pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sliding Through the Hood")
clock = pygame.time.Clock()
def draw_sky():
    image = pygame.image.load("rajvosa.jpg")  # Load the background image
    window.fill((0, 0, 0))  # Fill the window with black color
    window.blit(image)  # Draw the background image
def draw_rect():
    rect_width = 800
    rect_height = 150
    rect_x = 0
    rect_y = 600 - rect_height  # Position the rectangle at the bottom of the window
    pygame.draw.rect(window, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
            if event.key == pygame.K_PGUP:
                print("Space key pressed")
    draw_sky()
    draw_rect()
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS