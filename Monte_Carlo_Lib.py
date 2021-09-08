import numpy as np
import matplotlib.pyplot as plt


class Lattice:
    def __init__(self, nx, rho, fa):
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
            if np.random.random() > rho:
                all_particles[i] = "B"

        while len(all_particles) > 0:
            #To add the all_particles to the gridß

    def map(self):
        print(self.all_particles)
    
    def energy(self,eps_aa,eps_ab,eps_bb):
        energy = 0
        for i in range(len(self.grid)-1):
            for j in range(len(self.grid[0])-1):
                if self.grid[i][j] == "A":
                    #Energy if the vertex pair start with type A
                    if self.grid[i][j+1]=="A" or self.grid[i+1][j]=="A":
                        #aa pair for (vx,vy+1) and (vx+1,vy)
                        energy += eps_aa
                    elif self.grid[i][j+1]=="B" or self.grid[i+1][j]=="B":
                        #ab pair
                        energy += eps_ab
                elif self.grid[i][j] == "B":
                    if self.grid[i][j+1]=="A" or self.grid[i+1][j]=="A":
                        #ba pair
                        energy += eps_ab
                    elif self.grid[i][j+1]=="B" or self.grid[i+1][j]=="B":
                        #bb pair
                        energy += eps_bb
        return energy

