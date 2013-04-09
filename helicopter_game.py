import helicopter
import movingpic
import obstacles

heli_width=144
heli_height=53
heli_speed=20
canvas_speed=10
brick_width=100


heli=helicopter.Helicopter(0,0,heli_width,heli_height)
gif=movingpic.Picture(0)


def ceiling(x):
    (x_min,y_min,x_max,y_max)=agentsim.gui.get_canvas_coords()
    while x<x_max:
        block=obstacles.ceil(x,brick_width)
        x+=brick_width
def floor(x):
    (x_min,y_min,x_max,y_max)=agentsim.gui.get_canvas_coords()
    while x<x_max:
        block=obstacles.Floor(x,brick_width)
        x+=brick_width
def move_obstacles():
    ceils=set(obstacles.ceil.get_all_instances())
    floors=set(obstacles.Floor.get_all_instances())
    superset=ceils.union(floors)
    for s in superset:
        s.move_by(canvas_speed)
    
    ceil_last_block=max(ceils,key=lambda e:e._x)
    ceil_x=ceil_last_block._x+brick_width
    ceil_new_block=obstacles.ceil(ceil_x,brick_width)
    
    floor_last_block=max(floors,key=lambda e:e._x)
    floor_x=floor_last_block._x+brick_width
    floor_new_block=obstacles.Floor(floor_x,brick_width)


        


def do_init():
    canvas=agentsim.gui.get_canvas()
    (cx_min,cy_min,cx_max,cy_max)=agentsim.gui.get_canvas_coords()
    canvas.create_rectangle(cx_min,cy_min,cx_max,cy_max,tags="canvas")
    heli.set_x_coord(cx_max/2)
    heli.set_y_coord(cy_max/2)
    images=[agentsim.PhotoImage(file="heli_1.gif"),agentsim.PhotoImage(file="heli_2.gif"),agentsim.PhotoImage(file="heli_3.gif"),
            agentsim.PhotoImage(file="heli_4.gif")]
    gif.add_images(images)
    photo=gif.update_image()
    ceiling(0)
    floor(0)
    heli.create_helicopter(canvas,photo)
def do_step():
    collision()
    pic=gif.update_image()
    move_obstacles()
    heli.play(pic,heli_speed)
def notify(ev):
    if ev.type=='4':
        heli.button_pressed()
    elif ev.type=='5':
       heli.button_released()
# Outdated, no longer works
def collision():
    canvas=agentsim.gui.get_canvas()
    heli_x=heli.get_x_coord()
    heli_y=heli.get_y_coord()
    (heli_xl,heli_xr)=(heli_x-(heli_width/2),heli_x+(heli_width/2))
    (heli_yt,heli_yb)=(heli_y-(heli_height/2),heli_y+(heli_height/2))
    border=canvas.find_withtag("canvas")
    (x_min,y_min,x_max,y_max)=canvas.bbox(border[0])
    (y_min,y_max)=(agentsim.gui.clip_y(y_min),agentsim.gui.clip_y(y_max))
    #print("yt: "+str(heli_yt)+" yb: "+str(heli_yb)+" y_max: "+str(y_max))
    if heli_yt<y_min or heli_yb>y_max:
        agentsim.gui.do_shutdown()
    

if __name__ == "__main__":
    import agentsim
    agentsim.init(title="Helicopter", init_fn=do_init, step_fn=do_step)
    agentsim.gui._root.bind("<Button-1>",notify)
    agentsim.gui._root.bind("<ButtonRelease-1>",notify)
    agentsim.start()