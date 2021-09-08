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

class Sim:
    #nx is for size of the grid
    def __init__(self,nx,rho,fa):
        self.size = nx
        self.density = rho
        self.fraction = fa

    def particle_gen(self):
        self.grid = Lattice.grid(nx)
        self.particles = []
        #self.na/na is number of particles "a" and "b"  in this simulation
        self.na = self.size^2 * fa
        self.nb = self.size^2 * (1-fa)
        
        #assign random position to particles
        while len(self.particles) < (self.na+self.nb):
            random_p =[ np.random.randint(0,nx),np.random.randint(0,nx)]
            if self.grid[random_p[0][random_p[1]] != "0":
                    #in grid, a "0" means no occupation, "1" means particle occupied but not yet assigned identity
                    self.particles.append(Particle(*random_p,"1"))
        print(self.grid)
