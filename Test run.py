import Monte_Carlo_Lib as mc

lattice1 = mc.Lattice(10,0.2,0.7)
lattice1.map()
print(lattice1.energy(2,3,3))
