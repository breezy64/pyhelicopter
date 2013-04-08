import helicopter
heli_width=144
heli_height=53
speed=30


heli=helicopter.Helicopter(0,0,heli_width,heli_height)
def notify(ev):
    if ev.type=='4':
        heli.button_pressed()
    elif ev.type=='5':
       heli.button_released()

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


def do_init():
    canvas=agentsim.gui.get_canvas()
    (cx_min,cy_min,cx_max,cy_max)=agentsim.gui.get_canvas_coords()
    canvas.create_rectangle(cx_min,cy_min,cx_max,cy_max,tags="canvas")
    heli.set_x_coord(cx_max/2)
    heli.set_y_coord(cy_max/2)
    photo=agentsim.PhotoImage(file="helicopter.gif")
    heli.create_helicopter(canvas,photo)
def do_step():
    collision()
    heli.play(speed)
    

if __name__ == "__main__":
    import agentsim
    agentsim.init(title="Helicopter", init_fn=do_init, step_fn=do_step)
    agentsim.gui._root.bind("<Button-1>",notify)
    agentsim.gui._root.bind("<ButtonRelease-1>",notify)
    agentsim.start()