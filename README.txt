Helicopter Game:
	by: Byron Marony, Navjeet Dhaliwal, Edrick De Guzman 

Requirements:
  Tkinter 
  Python 3
Game Controls:
  right click to start
  left click to move helicopter
  q to quit

The main program is in helicopter_game.py

This game is optimized to run on the lab machines in 5-013
If you experience troubles with speed, you can alter the speed by doing the following:

  1. Go into agentsim.py and change the running speed (self._speed) in the do_run() method (line 213). Setting self._speed to a value of 120 is recommended
  2. Change score delay (line 81) in the do_step() function helicopter_game.py . The recommended delay value to use is 30 
  
  In most cases, changing the above two settings is enough to fix speed issues 
  However, if you still have speed troubles, you can also change the heli_speed, and canvas_speed variables (line 21 and line 23) in helicopter_game.py
  
  Acknowledgemnts:
 
  This webpage was very, very helpful for our project: http://effbot.org/tkinterbook/canvas.htm
  
  The gif images used for the helicopter were extracted from the gif located
  at this website: http://www.swish-designs.co.uk/index.php?pageid=33   
  
