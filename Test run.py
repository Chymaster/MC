import Monte_Carlo_Lib as mc

lattice1 = mc.Lattice(500,0.2,0.7)
print(lattice1.energy(2,3,3))
lattice1.map()
