import numpy as np


class Lattice:
    def __init__(self, nx, rho, fa, eps = (1,1,1)):
        # nx is for  Lattice.grid generates an array of size nx by nx
        # rho is the density of particles
        # fa is fraction of particles that's type 1 for A
        # eps is for energy per verdex pair, the order is (eps_aa,eps,ab,eps_ab)

        # Generating empty grid
        self.grid = np.zeros((nx, nx), int)
        self.grid_size = nx
        self.eps = eps
        ptc_n = int(rho * (nx ** 2))  # number of particles

        # Generate a list of particles
        all_particles = np.full(ptc_n, 1)
        # Filled up with A,
        # Now turn some of them into B
        for i in range(ptc_n):
            if np.random.random() > fa:
                all_particles[i] = 2
        all_particles = iter(all_particles)

        # Putting the particles in grid
        all_positions = np.indices((nx, nx)).reshape(2, -1).T  # a pool of positions in index [x,y]
        np.random.shuffle(all_positions)  # shuffle the pool
        for i in all_positions[
                 :ptc_n]:  # loop in the pool until all particle are filled ([:ptc_n] only keeps the first ptc_n number
            self.grid[i[0]][i[1]] = next(all_particles)

    def map(self):
        import matplotlib.patches as mpatches
        import matplotlib.pyplot as plt

        im = plt.imshow(self.grid)
        colors = [im.cmap(im.norm(value)) for value in [0, 1, 2]]
        patches = [mpatches.Patch(color=colors[0], label="Empty".format(l=0)),
                   mpatches.Patch(color=colors[1], label="Particle A".format(l=1)),
                   mpatches.Patch(color=colors[2], label="Particle B".format(l=2))]
        plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        plt.show()

    def energy(self, eps_aa, eps_ab, eps_bb):
        energy = 0
        # None boundary energy
        for i in range(len(self.grid) - 1):
            for j in range(len(self.grid[0]) - 1):
                if self.grid[i][j] == 1:
                    # Energy if the vertex pair start with type A
                    if self.grid[i][j + 1] == 1 or self.grid[i + 1][j] == 1:
                        # aa pair for (vx,vy+1) and (vx+1,vy)
                        energy += eps_aa
                    elif self.grid[i][j + 1] == 2 or self.grid[i + 1][j] == 2:
                        # ab pair
                        energy += eps_ab
                elif self.grid[i][j] == 2:
                    if self.grid[i][j + 1] == 1 or self.grid[i + 1][j] == 1:
                        # ba pair
                        energy += eps_ab
                    elif self.grid[i][j + 1] == 2 or self.grid[i + 1][j] == 2:
                        # bb pair
                        energy += eps_bb

            # Boundary energy

        return energy



    # An iterator pool of all possible positions in
    def position_pool(self):
        positionpool = np.indices((self.grid_size, self.grid_size)).reshape(2, -1).T
        np.random.shuffle(positionpool)
        return iter(positionpool)

    def swap(self):
        occupied = False
        pool = self.position_pool()
        pre_swap_energy = self.energy(*self.eps)
        while not occupied:
            position = next(pool)
            identity = self.grid[position[0]][position[1]]
            if identity != 0:
                target_position = next(pool)
                target_id = self.grid[target_position[0]][target_position[1]]
                self.grid[position[0]][position[1]] = target_id
                self.grid[target_position[0]][target_position[1]] = identity
                occupied = True
        if not self.accept():
            self.grid[position[0]][position[1]] = identity
            self.grid[target_position[0]][target_position[1]] = target_id


    # monte carlo algorithm
    def accept(self):

        return True