import helicopter 
import movingpic 
import blocks 
import random
 
heli_width=139
heli_height=53 
heli_speed=5 
canvas_speed=10 
brick_width=100
brick_limit=30
obstacle_limit=5
obstacle_width=25 
 
 
heli=helicopter.Helicopter(0,0,heli_width,heli_height) 
gif=movingpic.Picture(0)
loop_timer=blocks.Timer() 
 
 
def ceiling(x): 
    (x_min,y_min,x_max,y_max)=agentsim.gui.get_canvas_coords() 
    while x<x_max: 
        block=blocks.Ceil(x,brick_width) 
        x+=brick_width 
def floor(x): 
    (x_min,y_min,x_max,y_max)=agentsim.gui.get_canvas_coords() 
    while x<x_max: 
        block=blocks.Floor(x,brick_width) 
        x+=brick_width 
def move_obstacles(): 
    (x_min, y_min,x_max,y_max) = agentsim.gui.get_canvas_coords()    
    ceils = set(blocks.Ceil.get_all_instances()) 
    floors = set(blocks.Floor.get_all_instances())
    all_blocks = blocks.Block.get_all_instances() 
    
    superset=ceils.union(floors)
    for o in all_blocks:
        o.move_by(canvas_speed)
    if len(superset)<brick_limit:    
        ceil_last_block=max(ceils,key=lambda e:e._x) 
        ceil_x=ceil_last_block._x+brick_width 
        ceil_new_block=blocks.Ceil(ceil_x,brick_width) 
     
        floor_last_block=max(floors,key=lambda e:e._x) 
        floor_x=floor_last_block._x+brick_width 
        floor_new_block=blocks.Floor(floor_x,brick_width)
    canvas=agentsim.gui.get_canvas()
    o_blocks=len(canvas.find_withtag("obstacle"))  
    if o_blocks<obstacle_limit and loop_timer.get_time()%50==0:
        block = blocks.Obstacle(obstacle_width) 
 
 
def do_init(): 
    canvas=agentsim.gui.get_canvas() 
    (cx_min,cy_min,cx_max,cy_max)=agentsim.gui.get_canvas_coords()
    heli.set_x_coord(cx_max/2) 
    heli.set_y_coord(cy_max/2)
    print(cy_max/2-(heli_height/2)) 
    images=[agentsim.PhotoImage(file="heli_1.gif"),agentsim.PhotoImage(file="heli_2.gif"),agentsim.PhotoImage(file="heli_3.gif"), 
            agentsim.PhotoImage(file="heli_4.gif")] 
    gif.add_images(images) 
    photo=gif.update_image() 
    ceiling(0) 
    floor(0)
    #block = obstacles.Obstacle(obstacle_width) 
    heli.create_helicopter(canvas,photo) 
def do_step(): 
    collision() 
    pic=gif.update_image() 
    move_obstacles() 
    heli.play(pic,heli_speed)
    loop_timer.inc() 
def notify(ev): 
    print((ev.x,ev.y))    
    if ev.type=='4': 
        heli.button_pressed() 
    elif ev.type=='5': 
       heli.button_released() 
 
def collision(): 
    (x_min,y_min,x_max,y_max)=agentsim.gui.get_canvas_coords() 
    canvas=agentsim.gui.get_canvas() 
    heli_x=heli.get_x_coord() 
    heli_y=heli.get_y_coord() 
    (xl,xr,yt,yb)=(heli_x-(heli_width/2),heli_x+(heli_width/2),heli_y-(heli_height/2),heli_y+(heli_height/2))
    items=canvas.find_overlapping(xl,y_min,xr+obstacle_width,y_max) 
    for i in items: 
                
        tag=canvas.gettags(i)
        tag=tag[0] if tag else ''         
        
        if tag=="floor": 
           floor=blocks.Floor.get_instance_with_id(i)
           floor_y=floor._y
           if yb>floor_y:
               agentsim.gui._do_pause()
               agentsim.gui._root.bind("<Button-3>",lambda e:None)
         
        if tag=="ceiling":
           ceiling=blocks.Ceil.get_instance_with_id(i)
           ceiling_y=ceiling._y+ceiling._height
           if yt<ceiling_y:
               agentsim.gui._do_pause()
               agentsim.gui._root.bind("<Button-3>",lambda e:None)
        if tag=="obstacle":
            obstacle=blocks.Obstacle.get_instance_with_id(i)
            obs_xl=obstacle._x
            obs_xr=obs_xl+obstacle._width
            obs_yt=obstacle._y
            obs_yb=obs_yt+obstacle._height
            error_xl=355
            error_xr=386
            error_yb=32.5+yt
            if yt>=obs_yt and yb<=obs_yb:
                if xr>obs_xl:
                    print("xr: "+str(xr)+" obs_x: "+str(obs_x))                    
                    agentsim.gui._do_pause()                    
                    agentsim.gui._root.bind("<Button-3>",lambda e:None)  
            elif xr>obs_xr and xl<obs_xl:       
                if (yb>obs_yt and yt<obs_yt) or (yt<obs_yb and yb>obs_yb):
                    agentsim.gui._do_pause()                    
                    agentsim.gui._root.bind("<Button-3>",lambda e:None)               
                    
             
       
 
if __name__ == "__main__": 
    import agentsim 
    agentsim.init(title="Helicopter", init_fn=do_init, step_fn=do_step) 
    agentsim.gui._root.bind("<Button-1>",notify) 
    agentsim.gui._root.bind("<ButtonRelease-1>",notify) 
    agentsim.start()
