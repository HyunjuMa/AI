from pyrobot.simulators.pysim import *
import random

def overlaps(x, y, walls):
    buffer = 0.1
    for (x1, y1, x2, y2, color) in walls:
        if x1-buffer <= x <= x2+buffer and y1-buffer <= y <= y2+buffer:
            return True
    return False

def INIT():
    sim = TkSimulator((650, 650), (20,630), 60.0)
    pioneer1 = TkPioneer("Red Pioneer", 5, 5, 5.5,
                         ((.225, .225, -.225, -.225),
                          (.175, -.175, -.175, .175)), "red")
    sim.addRobot(60000, pioneer1)

    sim.robots[0].addDevice(Gripper())
    # add 16 sonars
    sim.robots[0].addDevice(Pioneer16Sonars())
    # add front light sensors
    sim.robots[0].addDevice(PioneerFrontLightSensors())


    # add the walls
    walls = [(8, 1.5, 8.5, 8.5, "antiquewhite"),
             (1.5, 1.5, 2, 8.5, "gray"),
             (1.5, 1, 8.5, 1.5, "antiquewhite3"),
             (1.5, 8.5, 8.5, 9, "antiquewhite3")
             ]
    for (x1, y1, x2, y2, color) in walls:
        sim.addBox(x1, y1, x2, y2, color, wallcolor=color)

    sim.addBox(2, 1.5, 3, 2.5)
    sim.addBox(2, 6.3, 2.5, 6.8)

    numpucks = 20
    for i in range(1, numpucks+1):
        x = random.uniform(2, 8)
        y = random.uniform(2, 8)
        # avoid putting puck inside a wall
        while overlaps(x, y, walls):
            x = random.uniform(1, 8)
            y = random.uniform(1, 8)
        puck = TkPuck("Puck%d" % i, x, y, 0,
                      ((.05, .05, -.05, -.05),
                       (.05, -.05, -.05, .05)), "red")
        sim.addRobot(None, puck)

    return sim
