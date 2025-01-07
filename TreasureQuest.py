from turtle import Turtle, Screen
#import turtle as t
import math

#setup the window/player screen
wn = Screen()
#win = tk.Tk()
wn.bgcolor('black') #color outside of map boundry
#wn.setup(1305,1305) #window size
#wn.screensize(1920,1080)
wn.setup(width = 1920, height = 1040)
#win.attributes('-fullscreen',True)
#win.title('TreasureQuest')
wn.bgpic('Data/Maps/main_map_day.gif') #game map

'''
Setup collision by coordinates
Collision works by creating 8 lists. 2 lists for each direction, North, South, East, West
We need 2 lists, one for x coordinates and one for y coordinates
if the player is moving perpendicular to the 2 lists of coordinates, they hit collision
if the player is moving parallel, they can move along the collision wall
if the player moves opposite of the collision, they can move
each pair of lists inhibits one direction of movement while letting the player move any of the other three
i.e if player is moving north and hits a southerly wall, they cannot move forward...
...but if they move south, east or west, they can move
'''
#a list of tuples for detecting collision if player is walking north
walk_north_collision = []
for i in range(-80,81):
    walk_north_collision.append(tuple((i,80)))
for i in range(-180,-79):
    walk_north_collision.append(tuple((i,20)))

#a list of tuples for detecting collision if player is walking south
walk_south_collision = []
for i in range(-80,81):
    walk_south_collision.append(tuple((i,100)))
for i in range(-180,-79):
    walk_south_collision.append(tuple((i,60)))
for i in range(-180,61):
    walk_south_collision.append(tuple((i,-40)))

#a list of tuples for detecting collision if the player is walking east
walk_east_collision = [(-200,40)]
for i in range(-60,81):
    walk_east_collision.append(tuple((60,i)))

#a list of tuples for detecting collision if the player is walking west
walk_west_collision = []
for i in range(40,81):
    walk_west_collision.append(tuple((-60,i)))


#setup the player
player = Turtle()
player.penup()
#get images for animations
#player animation moving north
wn.register_shape("Data/Characters/Sonic/sonic_north_01.gif") #player left foot
wn.register_shape("Data/Characters/Sonic/sonic_north_02.gif") #player right foot
wn.register_shape("Data/Characters/Sonic/sonic_north_03.gif") #player standing
#player animation moving south
wn.register_shape("Data/Characters/Sonic/sonic_south_01.gif") #player left foot
wn.register_shape("Data/Characters/Sonic/sonic_south_02.gif") #player right foot
wn.register_shape("Data/Characters/Sonic/sonic_south_03.gif") #player standing
#player animaton moving west
wn.register_shape("Data/Characters/Sonic/sonic_west_01.gif") #begin step
wn.register_shape("Data/Characters/Sonic/sonic_west_02.gif") #full stride
wn.register_shape("Data/Characters/Sonic/sonic_west_03.gif") #end step
wn.register_shape("Data/Characters/Sonic/sonic_west_04.gif") #standing
#player animation moving east
wn.register_shape("Data/Characters/Sonic/sonic_east_01.gif") #begin step
wn.register_shape("Data/Characters/Sonic/sonic_east_02.gif") #full stride
wn.register_shape("Data/Characters/Sonic/sonic_east_03.gif") #end step
wn.register_shape("Data/Characters/Sonic/sonic_east_04.gif") #standing
#player starting sprite
player.shape("Data/Characters/Sonic/sonic_east_04.gif") #Defult position for player at begin game

#wn.register_shape("grass_01.gif")
#grass = Turtle()
#grass.shape("grass_01.gif")

### SETUP FUNCTIONS for PLAYER MOVEMENT and CONTROLS ###
def walk_north():
    '''Moves the player north by 20 pixles. Called when the 'w' key is pressed.'''
    #first setup collision so player can't walk through walls
    #print(f'({int(player.xcor())},{int(player.ycor())})')
    player_pos = tuple(player.pos())
    if player_pos in walk_north_collision:
        print("collision")
        player.setheading(90)
        player.shape("Data/Characters/Sonic/sonic_north_01.gif")
        player.shape("Data/Characters/Sonic/sonic_north_02.gif")
        player.shape("Data/Characters/Sonic/sonic_north_03.gif")
        #for i in range(4):
            #player.undo()
        #if player.xcor() in collision_x:
            #for i in range(4):
                #player.undo()
            #print('collision triggered')
    else:
        player.setheading(90)
        player.speed(0) #slows the speed down so the anmations look nice. ...so apparently the speed changes based on monitor resolution...
        player.shape("Data/Characters/Sonic/sonic_north_01.gif")
        player.forward(10)
        player.shape("Data/Characters/Sonic/sonic_north_02.gif")
        player.forward(10)
        player.shape("Data/Characters/Sonic/sonic_north_03.gif")
        player.speed(0) #resets the speed to default so the transitions are smoother
    player.setpos((round(player.pos()[0])),(round(player.pos()[1]))) #fixed a bug where the player position would no be a whole number
    player_pos = tuple(player.pos())
    print(f'Player X; ',player_pos[0])
    print(f'Player Y; ',player_pos[1])

def walk_south():
    '''Moves the player south by 20 pixles. Called when the 's' key is pressed'''
    player_pos = tuple(player.pos())
    if player_pos in walk_south_collision:
        print("collision")
        player.shape("Data/Characters/Sonic/sonic_south_01.gif")
        player.shape("Data/Characters/Sonic/sonic_south_02.gif")
        player.shape("Data/Characters/Sonic/sonic_south_03.gif")
        #for i in range(4):
            #player.undo()
    else:
        player.setheading(270)
        player.speed(0) #slows the speed down so the anmations look nice
        player.shape("Data/Characters/Sonic/sonic_south_01.gif")
        player.forward(10)
        player.shape("Data/Characters/Sonic/sonic_south_02.gif")
        player.forward(10)
        player.shape("Data/Characters/Sonic/sonic_south_03.gif")
        player.speed(0) #resets the speed to default so the transitions are smoother
    player.setpos((round(player.pos()[0])),(round(player.pos()[1]))) #fixed a bug where the player position would no be a whole number
    player_pos = tuple(player.pos())
    print(f'Player X; ',player_pos[0])
    print(f'Player Y; ',player_pos[1])
    #print(f'({int(player.xcor())},{int(player.ycor())})')
    #if player.ycor() in collision_y:
        #if player.xcor() in collision_x:
            #for i in range(4):
                #player.undo()
            #print('collision triggered')

def walk_east():
    '''Moves the player east by 20 pixels. Called when the 'd' key is pressed'''
    player_pos = tuple(player.pos())
    if player_pos in walk_east_collision:
        print("collision")
        player.shape("Data/Characters/Sonic/sonic_east_01.gif")
        player.shape("Data/Characters/Sonic/sonic_east_02.gif")
        player.shape("Data/Characters/Sonic/sonic_east_03.gif")
        player.shape("Data/Characters/Sonic/sonic_east_04.gif")
            #for i in range(6):
                #player.undo()
    else:
        player.setheading(0)
        player.speed(3) #slows the speed down so the anmations look nice
        player.shape("Data/Characters/Sonic/sonic_east_01.gif")
        player.forward(5)
        player.shape("Data/Characters/Sonic/sonic_east_02.gif")
        player.forward(5)
        player.shape("Data/Characters/Sonic/sonic_east_03.gif")
        player.forward(5)
        player.shape("Data/Characters/Sonic/sonic_east_04.gif")
        player.forward(5)
        player.speed(0) #resets the speed to default so the transitions are smoother 
    player.setpos((round(player.pos()[0])),(round(player.pos()[1]))) #fixed a bug where the player position would no be a whole number
    player_pos = tuple(player.pos())
    print(f'Player X; ',player_pos[0])
    print(f'Player Y; ',player_pos[1])
    #print(f'({int(player.xcor())},{int(player.ycor())})')
    #if player.xcor() in collision_x:
        #print("in x coord")
        #if player.ycor() in collision_y:
            #for i in range(6):
                #player.undo()
            #print('collision triggered')

def walk_west():
    '''Moves the player west by 20 pixles. Called when the 'a' key is pressed'''
    player_pos = tuple(player.pos())
    if player_pos in walk_west_collision:
        print("collision")
        player.shape("Data/Characters/Sonic/sonic_west_01.gif")
        player.shape("Data/Characters/Sonic/sonic_west_02.gif")
        player.shape("Data/Characters/Sonic/sonic_west_03.gif")
        player.shape("Data/Characters/Sonic/sonic_west_04.gif")
        #for i in range(6):
            #player.undo()
    else:
        player.setheading(180)
        player.speed(3) #slows the speed down so the anmations look nice
        player.shape("Data/Characters/Sonic/sonic_west_01.gif")
        player.forward(5)
        player.shape("Data/Characters/Sonic/sonic_west_02.gif")
        player.forward(5)
        player.shape("Data/Characters/Sonic/sonic_west_03.gif")
        player.forward(5)
        player.shape("Data/Characters/Sonic/sonic_west_04.gif")
        player.forward(5)
        player.speed(0) #resets the speed to default so the transitions are smoother
    player.setpos((round(player.pos()[0])),(round(player.pos()[1]))) #fixed a bug where the player position would no be a whole number
    player_pos = tuple(player.pos())
    print(f'Player X; ',player_pos[0])
    print(f'Player Y; ',player_pos[1])
    #print(f'({int(player.xcor())},{int(player.ycor())})')
    #if player.xcor() in collision_x:
        #print("in x coord")
        #if player.ycor() in collision_y:
            #for i in range(6):
                #player.undo()
            #print('collision triggered')

def travel():
    '''Moves the player forward continuously. Useful for sliding on ice or driving in a car, riding a horse, etc...'''
    player.forward(speed)
    wn.ontimer(travel, 10)

def endgame():
    '''Ends game with a key input'''
    wn.bye()

### KEY BINDINGS ###
#player movement
wn.onkey(walk_north, 'w')
wn.onkey(walk_south, 's')
wn.onkey(walk_east, 'd')
wn.onkey(walk_west, 'a')
#close game
wn.onkey(endgame, 'Escape')

#Must be used with key bindings so that the game can detect key presses constantly
wn.listen()


#Original binding for the player when they move continuously. Not used in this game but saving for future reference.
#wn.onkey(lambda: player.setheading(90), 'Up')
#wn.onkey(lambda: player.setheading(180), 'Left')
#wn.onkey(lambda: player.setheading(0), 'Right')
#wn.onkey(lambda: player.setheading(270), 'Down')
#player_pos = tuple(player.pos())
if tuple(player.pos()) == (0,0):
    print("Origin 0,0")



#travel() #makes the player move forward continuously. Not used in this game but saving for future reference.

wn.mainloop() #Starts event loop - calling Tkinter's mainloop function. Must be last statement!
quit() #closes window and shuts down kernel after mainloop has been ended by player