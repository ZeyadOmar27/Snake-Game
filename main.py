import tkinter as tk
import random

def main():
    global snake_initial_position_x, snake_initial_position_y, food_initial_position_x, food_initial_position_y, snake_body, velocity_x, velocity_y, game_over, score
    
    draw()
    
    def restart(event):  # Define restart logic inside main()
        global snake_initial_position_x, snake_initial_position_y, food_initial_position_x, food_initial_position_y, snake_body, velocity_x, velocity_y, game_over, score
        
        snake_initial_position_x = 5 * TILE_SIZE
        snake_initial_position_y = 5 * TILE_SIZE
        food_initial_position_x = 10 * TILE_SIZE
        food_initial_position_y = 10 * TILE_SIZE
        snake_body = []
        velocity_x = 0
        velocity_y = 0
        game_over = False
        score = 0
        move()  # Restart the game loop

    window.bind("<space>", restart)  # Now Space key correctly restarts the game
    window.bind("<KeyPress>", change_direction)
    window.mainloop()



#Game Settings
ROWS = 25
COLUMNS = 25
TILE_SIZE = 25
WINDOW_HEIGHT = TILE_SIZE * COLUMNS
WINDOW_WIDTH = TILE_SIZE * ROWS

#Game Window
window = tk.Tk()
window.title("••• 𝐒𝐍𝐀𝐊𝐄 •••")
window.resizable(False, False)

#Canvas
canvas = tk.Canvas(window, bg = "#000011", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 4, highlightthickness = 4)
canvas.pack()
window.update()

#Center The Window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Initialize Game
snake_initial_position_x = 5 * TILE_SIZE #Initial position_x for snake head
snake_initial_position_y = 5 * TILE_SIZE #Initial position_x for snake head
food_initial_position_x = 10 * TILE_SIZE #Initial position_x for food
food_initial_position_y = 10 * TILE_SIZE #Initial position_y for food
snake_body = [] #Multiple snake tiles
velocity_x = 0
velocity_y = 0
game_over = False
score = 0

def change_direction(e):
    global velocity_x, velocity_y

    key = e.keysym
    if(key == "Up" and velocity_y != 1):
        velocity_x = 0
        velocity_y = -1
    elif(key == "Down" and velocity_y != -1):
        velocity_x = 0
        velocity_y = 1
    elif(key == "Left" and velocity_x != 1):
        velocity_x = -1
        velocity_y = 0
    elif(key == "Right" and velocity_x != -1):
        velocity_x = 1
        velocity_y = 0


def move():
    global velocity_x, velocity_y, snake_initial_position_x, snake_initial_position_y, food_initial_position_x, food_initial_position_y, score, game_over, snake_body

    #GameOver
    if (snake_initial_position_x <= 0) or (snake_initial_position_y <= 0) or (snake_initial_position_x >= window_width) or (snake_initial_position_y >= window_height):
        game_over = True

    if (snake_initial_position_x, snake_initial_position_y) in snake_body:
        game_over = True
        
    if game_over:
        return

    
    #collision
    if(snake_initial_position_x == food_initial_position_x) and (snake_initial_position_y == food_initial_position_y):
        snake_body.append((food_initial_position_x, food_initial_position_y))
        food_initial_position_x = random.randint(1, COLUMNS - 1) * TILE_SIZE
        food_initial_position_y = random.randint(1, ROWS - 1) * TILE_SIZE
        score +=1

    while (food_initial_position_x, food_initial_position_y) in snake_body:
        food_initial_position_x = random.randint(1, COLUMNS - 1) * TILE_SIZE
        food_initial_position_y = random.randint(1, ROWS - 1) * TILE_SIZE
    
    # Update the snake body from tail to head
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i] = snake_body[i - 1]  # Each body part moves to the position of the one before it

    # First body part follows the head
    if snake_body:
        snake_body[0] = (snake_initial_position_x, snake_initial_position_y)


    snake_initial_position_x += velocity_x * TILE_SIZE
    snake_initial_position_y += velocity_y * TILE_SIZE


def draw():
    move()
    canvas.delete("all")
    # draw the initial position for food
    canvas.create_rectangle(food_initial_position_x, food_initial_position_y, food_initial_position_x + TILE_SIZE, food_initial_position_y + TILE_SIZE, outline="#4B0000", width = 3, fill = "#DC143C")
    
    
    # draw the snake's head
    canvas.create_rectangle(snake_initial_position_x, snake_initial_position_y, snake_initial_position_x + TILE_SIZE, snake_initial_position_y + TILE_SIZE, outline="green", width = 8, fill = "lime green")
    window.after(100, draw) # 100ms = 10fps
    
    # draw the snake's rest body parts
    for x, y in snake_body:
        canvas.create_rectangle(x, y, x + TILE_SIZE, y + TILE_SIZE, outline="green", width = 8, fill = "lime green")
    
    #GameOver text
    if game_over:
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2,font = "Arial 20", text = f"Game Over: {score}",fill = "white")
    else:
        canvas.create_text(50,20, font = "Ariel 15", text = f"Score: {score}",fill = "white")


if __name__ == "__main__":
    main()