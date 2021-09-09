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
        ptc_n = int(rho*(nx**2)) #number of particles

        #Generate a list of particles
        all_particles = np.full(ptc_n,'A')
        #Filled up with A,
        #Now turn some of them into B
        for i in range(ptc_n):
            if np.random.random() > fa:
                all_particles[i] = "B"
        all_particles = iter(all_particles)

        #Putting the particles in grid
        all_positions = np.indices((nx,nx)).reshape(2,-1).T  #a pool of positions in indexl [x,y]
        np.random.shuffle(all_positions)  #shuffle the pool
        for i in all_positions[:ptc_n]:  #loop in the pool until all particle are filled ([:ptc_n] only keeps the first ptc_n number
                self.grid[i[0]][i[1]] = next(all_particles)




    def map(self):
        print(self.grid)
        #plt.imshow(self.grid)
        #Doesn't work bc self.grid is str array
        #plt.show()
    
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

