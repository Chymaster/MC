import numpy as np
import matplotlib.pyplot as plt
#Hello
class Particle:
    def __init__(self,x,y,identity="a"):
        #self.p for position
        self.p = np.array((x,y))
        self.identity = identity

class Latice:
    def __init__(self,nx):
        # Lattice.grid generates an array of size nx by nx
        self.grid = np.zeros((nx,nx),str)
        self.particles = []

    def type(self,x,y):
        return self.grid[x][y]

    def add(self,x,y,identity):
        if self.grid[x][y] = "0":
            self.grid[x][y] = identity
            self.particles.append(Particle(x,y,identity))

    def swap(self,x,y,target_x,target_y):
        self.grid[x][y]
        


