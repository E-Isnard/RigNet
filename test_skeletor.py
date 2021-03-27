import skeletor as sk
import numpy as np
import trimesh as tr
import navis

mesh = tr.load_mesh("quick_start/17872_remesh.obj")
cont = sk.contract(mesh,iter_lim=4)
swc = sk.skeletonize(cont, method='edge_collapse')
print(swc)

# meshneuron = navis.MeshNeuron(mesh, units='8nm')
# # navis.plot3d([skeleton, meshneuron], color=[(1, 0, 0), (1, 1, 1, .1)])
# nl = navis.example_neurons(n=3, kind='skeleton')
# fig = nl.plot3d()
