import helicopter

heli_width=50
heli_height=25

heli=helicopter.Helicopter(0,0,heli_width,heli_height)
def notify(ev):
    print(ev.type)
    if ev.type=='4':
        heli.button_pressed()
    elif ev.type=='5':
       heli.button_released()
def do_init():
    canvas=agentsim.gui.get_canvas()
    (cx_min,cy_min,cx_max,cy_max)=agentsim.gui.get_canvas_coords()
    heli.set_x_coord(cx_max/2)
    heli.set_y_coord(cy_max/2)
    heli.create_helicopter(canvas)
def do_step():
    heli.play()

if __name__ == "__main__":
    import agentsim
    agentsim.init(title="Helicopter", init_fn=do_init, step_fn=do_step)
    agentsim.gui._root.bind("<Button-1>",notify)
    agentsim.gui._root.bind("<ButtonRelease-1>",notify)
    agentsim.start()