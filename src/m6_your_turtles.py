"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and James Werne.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################


import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(20)

bro1 = rg.SimpleTurtle()
bro1.pen = rg.Pen('midnight blue', 8)
bro1.speed = 10

bro2 = rg.SimpleTurtle()
bro2.pen = rg.Pen('red', 4)
bro2.speed = 10

for k in range(40):
    bro1.forward(k)
    bro1.left(50 - k)
    bro1.forward(8)

for k in range(20):
    bro2.forward(10*k)
    bro2.left(90 + k)


window.close_on_mouse_click()