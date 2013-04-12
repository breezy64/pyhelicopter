#    CMPUT 297/115 - Helicopter Game - helicopter_game.py - Due 2013-04-12
#                                                                                  
#    Version 3.0 2013-04-13                                            
#                                                                      
#    By: Byron Maroney                                                 
#        Edrick de Guzman
#        Navjeet Dhaliwal                                              
#                                                                       
#                                                                      
#   This assignment has been done under the full collaboration model,  
#   and any extra resources are cited in the code below.       


import helicopter 
import movingpic 
import blocks 
import random
import enemies
 
# heli_speed controls the speed at which the helicopter moves up and down
heli_speed=5 
# canvas speed controls the speed of the floor, ceiling, and obstacles
canvas_speed=10 
# brick_width is the width of an individual ceiling/floor unit
brick_width=100
# brick_limit sets the limit for number of instances of ceiling/floor objects
brick_limit=30
# onstacle_limit limits the number of obstacle objects
obstacle_limit=5
obstacle_width=25

# Position the higscore counter
xpos = 750
ypos = 20
increment = 100 
 
# Initialize a bunch of objects 
heli=helicopter.Helicopter(0,0) 
gif=movingpic.mPicture(0)
loop_timer=blocks.Timer()
highscore = blocks.Score(xpos,ypos)

heli_width=heli.get_width()
heli_height=heli.get_height()
 
 

 
 
def do_init(): 
    canvas=agentsim.gui.get_canvas() 
    (cx_min,cy_min,cx_max,cy_max)=agentsim.gui.get_canvas_coords()
    # Put helicopter at the center of screen
    heli.set_x_coord(cx_max/2) 
    heli.set_y_coord(cy_max/2)
    # The original gif is from http://www.swish-designs.co.uk/index.php?pageid=33     
    images=[agentsim.PhotoImage(file="heli_1.gif"),agentsim.PhotoImage(file="heli_2.gif"),agentsim.PhotoImage(file="heli_3.gif"), 
            agentsim.PhotoImage(file="heli_4.gif")] 
    # Load helicopter images into motion picture class
    gif.add_images(images) 
    photo=gif.update_image() 
    #initialize floor and ceiling
    ceiling(0) 
    floor(0) 
    # Add references to the canvas to classes that need them
    heli.create_helicopter(canvas,photo)
    highscore.add_canvas(canvas) 
def do_step(): 
    collision() 
    #Cycle to the next image of the helicopter    
    pic=gif.update_image() 
    move_enemies()
    move_obstacles() 
    # move helicopter    
    heli.play(pic,heli_speed)
    #increment loop timer and highscore   
    loop_timer.inc()
    highscore.inc(increment)
    highscore.drawtime()
    # delay to make score appear and re-appear without drawover
    agentsim.gui._root.after(1,highscore.hide)
def notify(ev): 
    # Monitor the state of left_mouse     
    
    # Type 4==left mouse pressed    
    if ev.type=='4': 
        heli.button_pressed() 
    # Type 5==left mouse released     
    elif ev.type=='5': 
       heli.button_released() 
def ceiling(x): 
    # make the ceiling    
    (x_min,y_min,x_max,y_max)=agentsim.gui.get_canvas_coords() 
    while x<x_max: 
        block=blocks.Ceil(x,brick_width) 
        x+=brick_width 
def floor(x): 
    # Make the floor    
    (x_min,y_min,x_max,y_max)=agentsim.gui.get_canvas_coords() 
    while x<x_max: 
        block=blocks.Floor(x,brick_width) 
        x+=brick_width 
def move_obstacles(): 
    (x_min, y_min,x_max,y_max) = agentsim.gui.get_canvas_coords()    
    # Get all the obstacles that need to be manipulated    
    ceils = set(blocks.Ceil.get_all_instances()) 
    floors = set(blocks.Floor.get_all_instances())
    all_blocks = blocks.Block.get_all_instances() 
    
    superset=ceils.union(floors)
    for o in all_blocks:
        o.move_by(canvas_speed)
    # Add more ceiling and floor bricks if the number of bricks is less than brick_limit    
    if len(superset)<brick_limit:    
        ceil_last_block=max(ceils,key=lambda e:e._x) 
        ceil_x=ceil_last_block._x+brick_width 
        #Add the next ceiling brick directly after the last ceiling_brick        
        ceil_new_block=blocks.Ceil(ceil_x,brick_width) 
        #Repeat the above procedure for floor bricks
        floor_last_block=max(floors,key=lambda e:e._x) 
        floor_x=floor_last_block._x+brick_width 
        floor_new_block=blocks.Floor(floor_x,brick_width)
    canvas=agentsim.gui.get_canvas()
    o_blocks=len(canvas.find_withtag("obstacle"))  
    #space out the positioning of obstacles using a timer    
    if o_blocks<obstacle_limit and loop_timer.get_time()%50==0:
        block = blocks.Obstacle(obstacle_width) 
def move_enemies():
    (x_min, y_min,x_max,y_max) = agentsim.gui.get_canvas_coords()
    #get instances of every enemy    
    rockets = set(enemies.Rocket.get_all_instances())
    missiles = set(enemies.Missile.get_all_instances())
    lasers = set(enemies.Laser.get_all_instances())
    #after certain time spawn enemies
    if loop_timer.get_time() > 300 and loop_timer.get_time() < 400:
        #one rocket at a time        
        if len(rockets) < 1:
            new_rocket = enemies.Rocket(heli.y_coord)
    if loop_timer.get_time() > 400 and loop_timer.get_time() < 500:
        #one missile at a time        
        if len(missiles) < 1:
            new_missile = enemies.Missile(heli.y_coord)
    if loop_timer.get_time() > 800:
        #one laser at a time at certain interval        
        if loop_timer.get_time() % 100 == 0:
            if len(lasers) < 1:
                new_laser = enemies.Laser()
    #call move function for enemies on screen    
    for r in rockets:
        r.move_by()
    for m in missiles:
        m.move_by(heli.y_coord)
    for l in lasers:
        l.move_by(heli.y_coord)
def collision(): 
    # Collision() approximates the helicopter by a rectangle
    # This approximates sometimes results in a collision with "white space"    
    (x_min,y_min,x_max,y_max)=agentsim.gui.get_canvas_coords() 
    canvas=agentsim.gui.get_canvas() 
    heli_x=heli.get_x_coord() 
    heli_y=heli.get_y_coord() 
    # Center the bounding box    
    (xl,xr)=(heli_x-(heli_width/2),heli_x+(heli_width/2))  
    (yt,yb)=heli_y-(heli_height/2)+6.5,heli_y+(heli_height/2)
    #Find all the items within bounding box the encompasses the rectangle    
    items=canvas.find_overlapping(xl,yt,xr,yb)
 
    for i in items: 
        # get all the tags associated with i         
        tags=canvas.gettags(i)        
        # Get the tag of the item from the tuple tags        
        tag=tags[0] if tags else ''         
        # if it's colliding with anything we care about, end the game         
        if tag == "laser" or tag == "rocket" or tag == "missile" or tag == "obstacle" or tag == "ceiling" or tag == "floor":
            endgame() 
        
def endgame():
     highscore.dispscore()
     # pause the simulation
     agentsim.gui._do_pause()                    
     # disable the start button
     agentsim.gui._root.bind("<Button-3>",lambda e:None)
            
       
 
if __name__ == "__main__": 
    import agentsim 
    agentsim.init(title="Helicopter", init_fn=do_init, step_fn=do_step) 
    agentsim.gui._root.bind("<Button-1>",notify) 
    agentsim.gui._root.bind("<ButtonRelease-1>",notify) 
    agentsim.start()
