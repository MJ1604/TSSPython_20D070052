import pygame as py, sys, time, random

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
Pos_of_Snake = [100, 50]
Body_of_Snake = [[100, 50], [85, 50], [70, 50]]
direction = 'R'

#Parameters for food
Pos_of_Food = [360,240]
food_spawn = False

score = 0


# Initialise game window
py.init()
py.display.set_caption('Snake Eater')
Window_of_Game = py.display.set_mode((frame_size_x, frame_size_y))
Window_of_Game.fill((0,0,0))

# FPS (frames per second) controller to set the speed of the game
fps_controller = py.time.Clock()




def check_for_events():

    global frame_size_x
    global frame_size_y 
    global direction
    global Rect_of_Food
    global food_spawn
    global score
    global Pos_of_Snake
    global Body_of_Snake
    global Pos_of_Food
    global Window_of_Game
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """
    for event in py.event.get():
        if event.type==py.QUIT:
            py.quit(0)           #To close program if someone closes window
            sys.exit(0)
        elif event.type==py.KEYDOWN:      #Taking input and applying it to change direction
            if event.key==py.K_UP and direction!='D':
                direction='U'
            elif event.key==py.K_DOWN and direction!='U':
                direction='D'
            elif event.key==py.K_LEFT and direction!='R':
                direction='L'
            elif event.key==py.K_RIGHT and direction!='L':
                direction='R'


def update_snake():

    global frame_size_x
    global frame_size_y 
    global direction
    global Rect_of_Food
    global food_spawn
    global score
    global Pos_of_Snake
    global Body_of_Snake
    global Pos_of_Food
    global Window_of_Game
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake's head move in the expected direction
    if direction=='U':
        Pos_of_Snake[1]-=10

    elif direction=='D':
        Pos_of_Snake[1]+=10

    elif direction=='L':
        Pos_of_Snake[0]-=10

    elif direction=='R':
        Pos_of_Snake[0]+=10

   

    Body_of_Snake.insert(0,Pos_of_Snake.copy())    #Inserting the new head position in body
    
    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.

    if (Pos_of_Snake[0]==Pos_of_Food[0] and Pos_of_Snake[1]==Pos_of_Food[1]):

        score+=1
        food_spawn=True
        create_food()
        
    else:
        
        Body_of_Snake.pop()     #Removing the last part of the body


    # End the game if the snake collides with the wall or with itself. 
    
    if (Pos_of_Snake[0]>710 or Pos_of_Snake[0]<0 or Pos_of_Snake[1]>470 or Pos_of_Snake[1]<0):
        game_over()                 #if snake collides with walls

    if (Pos_of_Snake in Body_of_Snake[1:] ):
        game_over()                 #if snake touches itself

    Window_of_Game.fill((0,0,0))          

def create_food():

    global frame_size_x
    global frame_size_y 
    global direction
    global Rect_of_Food
    global food_spawn
    global score
    global Pos_of_Snake
    global Body_of_Snake
    global Pos_of_Food
    global Window_of_Game

    
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    if (food_spawn==True):
        while Pos_of_Food in Body_of_Snake:    # food not on body
            Pos_of_Food = [random.randrange(0,710,10),random.randrange(0,470,10)]
        food_spawn==False

def show_score(pos, color, font, size):

    global frame_size_x
    global frame_size_y 
    global direction
    global Rect_of_Food
    global food_spawn
    global score
    global Pos_of_Snake
    global Body_of_Snake
    global Pos_of_Food
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    Img_of_Score=py.font.SysFont('Arial',size).render('Score- '+str(score),True,(0,0,255))
    Rect_of_Score=Img_of_Score.get_rect()
    Rect_of_Score.centerx=pos[0]
    Rect_of_Score.centery=pos[1]
    return(Img_of_Score,Rect_of_Score)


def update_screen():

    global frame_size_x
    global frame_size_y 
    global direction
    global Rect_of_Food
    global food_spawn
    global score
    global Pos_of_Snake
    global Body_of_Snake
    global Pos_of_Food
    global Window_of_Game
    """
    Draw the snake, food, background, score on the screen
    """
    for Body_of_Snake_pos in Body_of_Snake:
        Body_of_Snake_box=py.Rect(Body_of_Snake_pos[0],Body_of_Snake_pos[1],10,10)
        py.draw.rect(Window_of_Game,(255,165,0),Body_of_Snake_box)

    Food_of_Snake=py.Rect(Pos_of_Food[0],Pos_of_Food[1],10,10)
    py.draw.rect(Window_of_Game,(0,255,0),Food_of_Snake)
    Score=show_score((50,30),(0,0,255),'Arial',25)
    Window_of_Game.blit(Score[0],Score[1])

    py.display.flip()


def game_over():

    global frame_size_x
    global frame_size_y 
    global direction
    global Rect_of_Food
    global food_spawn
    global score
    global Pos_of_Snake
    global Body_of_Snake
    global Pos_of_Food
    global Window_of_Game
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    Img_of_Game_Over=py.font.SysFont('Arial',50).render('Game Over, Better luck next time',True,(255,0,0))
    Rect_of_Game_Over=Img_of_Game_Over.get_rect()
    Rect_of_Game_Over.centerx=360                      #position of game over 
    Rect_of_Game_Over.centery=240

    Window_of_Game.fill((0,0,0))
    Window_of_Game.blit(Img_of_Game_Over,Rect_of_Game_Over)

    score=show_score((360,175),(0,0,255),'Arial',25)    
    Window_of_Game.blit(score[0],score[1])

    py.display.flip()
    time.sleep(3)
    sys.exit(0)



# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run


    check_for_events()
    update_snake()
    update_screen()

    # To set the speed of the screen
    fps_controller.tick(10)
