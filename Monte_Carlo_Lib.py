import numpy as np
import matplotlib.pyplot as plt
#Hello
class Lattice:
    def __init__(self,nx,rho,fa):
        #nx is for  Lattice.grid generates an array of size nx by nx
        #rho is the density of particles 
        #fa is fraction of particles that's type "A"

        #Generating empty grid
        self.grid = np.zeros((nx,nx),str)
        self.grid_size = nx

        #Now filling the particles in
        all_particles = np.full(int(rho*(nx**2)),'A')
        #Filled up with A,
        #Now turn some of them into B
        for i in range(len(all_particles)):
            if np.random.random > rho:
                all_particles[i] = "B"
    
    def energy(self,eps_aa,eps_ab,eps_bb)

