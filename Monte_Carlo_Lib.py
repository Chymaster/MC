import numpy as np


class Lattice:
    def __init__(self, nx, rho, fa):
        #nx is for  Lattice.grid generates an array of size nx by nx
        #rho is the density of particles 
        #fa is fraction of particles that's type 1 for A

        #Generating empty grid
        self.grid = np.zeros((nx,nx),int)
        self.grid_size = nx
        ptc_n = int(rho*(nx**2)) #number of particles

        #Generate a list of particles
        all_particles = np.full(ptc_n,1)
        #Filled up with A,
        #Now turn some of them into B
        for i in range(ptc_n):
            if np.random.random() > fa:
                all_particles[i] = 2
        all_particles = iter(all_particles)

        #Putting the particles in grid
        all_positions = np.indices((nx,nx)).reshape(2,-1).T  #a pool of positions in indexl [x,y]
        np.random.shuffle(all_positions)  #shuffle the pool
        for i in all_positions[:ptc_n]:  #loop in the pool until all particle are filled ([:ptc_n] only keeps the first ptc_n number
                self.grid[i[0]][i[1]] = next(all_particles)





    def map(self):
        import matplotlib.patches as mpatches
        import matplotlib.pyplot as plt

        im = plt.imshow(self.grid)
        colors = [im.cmap(im.norm(value)) for value in [0,1,2]]
        patches = [mpatches.Patch(color=colors[0], label="Empty".format(l=0)), mpatches.Patch(color=colors[1], label="Particle A".format(l=1)),mpatches.Patch(color=colors[2], label="Particle B".format(l=2))]
        plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        plt.show()
    
    def energy(self,eps_aa,eps_ab,eps_bb):
        energy = 0
        for i in range(len(self.grid)-1):
            for j in range(len(self.grid[0])-1):
                if self.grid[i][j] == 1:
                    #Energy if the vertex pair start with type A
                    if self.grid[i][j+1]==1 or self.grid[i+1][j]== 1:
                        #aa pair for (vx,vy+1) and (vx+1,vy)
                        energy += eps_aa
                    elif self.grid[i][j+1]==2 or self.grid[i+1][j]==2:
                        #ab pair
                        energy += eps_ab
                elif self.grid[i][j] == 2:
                    if self.grid[i][j+1]==1 or self.grid[i+1][j]==1:
                        #ba pair
                        energy += eps_ab
                    elif self.grid[i][j+1]==2 or self.grid[i+1][j]==2:
                        #bb pair
                        energy += eps_bb
        return energy

    def swap(self):
        occupied = False
        while not occupied:
            position = np.random.randint(0,self.grid_size,size=(1,2))
            if self.grid[position[0]][position[1]] != 0:
                occupied = True
