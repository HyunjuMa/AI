# robot goes forward and then slows to a stop when it detects something  
   
from pyrobot.brain import Brain  
from pyrobot.brain.behaviors import *
   
class Avoid(Brain):  
           
   # Give the front two sensors, decide the next move  
   def determineMove(self, front, left, right):  
      if front < 0.8:
         if front < 0.4 or right < 0.6:
            print "front- go backward.."
            return (-1.2, -1.2) 
         elif left < 0.6: 
            print "front-left- go backward.."
            return (-0.5, 0.0)  
         else:
            print "obstacle ahead, hard turn"  
            return(0.1, -.4)  
      elif left < 0.8:
         if left < 0.4:
            print "left-"
            return (0.5, 0.0)
         else:
            print "object detected on left, slow turn"
            return(0.1, -0.3)  
      elif right < 0.8: 
         # if right < 0.4:
         #    print "right- go backward.."
         #    return (0.5, 0.0)
         # else:
         print "object detected on right, slow turn" 
         return(0.1, .3)  
      else:  
         return(0.5, 0.0) 
      
   def step(self):  
      front = min([s.distance() for s in self.robot.range["front"]])
      # for s in self.robot.range["front"]:
      #    print s.angle()
      # self.robot.simulation[0].name()
      left = min([s.distance() for s in self.robot.range["left-front"]])
      right = min([s.distance() for s in self.robot.range["right-front"]])
      translation, rotate = self.determineMove(front, left, right)  
      self.robot.move(translation, rotate)
      # self.robot.move('grab')

def INIT(engine): 
   assert (engine.robot.requires("range-sensor") and
           engine.robot.requires("continuous-movement"))
   return Avoid('Avoid', engine) 