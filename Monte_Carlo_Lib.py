import numpy as np


class Lattice:
    def __init__(self, nx, rho, fa):
        # nx is for  Lattice.grid generates an array of size nx by nx
        # rho is the density of particles
        # fa is fraction of particles that's type 1 for A
        # eps is for energy per verdex pair, the order is (eps_aa,eps,ab,eps_ab)

        # Generating empty grid
        self.grid_size = nx

        # Generate a list of particles
        particle_n = int(rho * (nx ** 2))  # number of particles
        all_particles = np.full(particle_n, 1)
        # Filled up with A,
        # Now turn some of them into B
        for i in range(particle_n):
            if np.random.random() > fa:
                all_particles[i] = 2
        all_particles = iter(all_particles)

        # Grid with random particle configuration
        grid = np.zeros((nx, nx), int)
        all_positions = np.indices((nx, nx)).reshape(
            2, -1).T  # a pool of positions in index [x,y]
        np.random.shuffle(all_positions)  # shuffle the pool
        # loop in the pool until all particle are filled ([:particle_n] only keeps the first particle_n number
        for i in all_positions[:particle_n]:
            grid[i[0]][i[1]] = next(all_particles)

        self.grid = grid

    def energy(self, eps_aa, eps_ab, eps_bb):
        energy = 0

        # A check position function is added for ease of periodic boundary conditions
        def check_position(x, y):
            if x < 0:
                x = self.grid_size - x
            if y < 0:
                y = self.grid_size - y
            if x >= self.grid_size:
                x = x - self.grid_size
            if y >= self.grid_size:
                y = y - self.grid_size
            return self.grid[x][y]

        #This checks positions x = 0...nx-1
        #Each pair of particle only contribute to energy once, therefore it is sufficient only to check energy for [x+1,y] and [x,y+1]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if check_position(i, j) == 1:
                    # Energy if the vertex pair start with type A
                    if check_position(i, j+1) == 1 or check_position(i+1, j) == 1:
                        # aa pair for (vx,vy+1) and (vx+1,vy)
                        energy += eps_aa
                    elif check_position(i, j+1) == 2 or check_position(i+1, j) == 2:
                        # ab pair
                        energy += eps_ab
                elif check_position(i, j) == 2:
                    if check_position(i, j+1) == 1 or check_position(i+1, j) == 1:
                        # ba pair
                        energy += eps_ab
                    elif check_position(i, j + 1) == 2 or check_position(i + 1, j) == 2:
                        # bb pair
                        energy += eps_bb

        return energy

    # An iterator pool of all possible positions in random order in [[x1,y1],[x2,y2]...]

    def position_pool(self):
        positionpool = np.indices(
            (self.grid_size, self.grid_size)).reshape(2, -1).T
        np.random.shuffle(positionpool)
        return iter(positionpool)

    def swap(self):
        occupied = False
        pool = self.position_pool()
        pre_swap_energy = self.energy(*self.eps)
        while not occupied:
            original_position = next(pool)
            identity = self.grid[original_position[0]][original_position[1]]
            if identity != 0:
                target_position = next(pool)
                target_id = self.grid[target_position[0]][target_position[1]]
                self.grid[original_position[0]
                          ][original_position[1]] = target_id
                self.grid[target_position[0]][target_position[1]] = identity
                occupied = True
        if not self.accept():
            self.grid[original_position[0]][original_position[1]] = identity
            self.grid[target_position[0]][target_position[1]] = target_id

    # monte carlo algorithm

    def accept(self):

        return True

    def map(self):
        import matplotlib.patches as mpatches
        import matplotlib.pyplot as plt

        im = plt.imshow(self.grid)
        colors = [im.cmap(im.norm(value)) for value in [0, 1, 2]]
        patches = [mpatches.Patch(color=colors[0], label="Empty".format(l=0)),
                   mpatches.Patch(color=colors[1],
                                  label="Particle A".format(l=1)),
                   mpatches.Patch(color=colors[2], label="Particle B".format(l=2))]
        plt.legend(handles=patches, bbox_to_anchor=(
            1.05, 1), loc=2, borderaxespad=0.)

        plt.show()
