import numpy as np
import matplotlib.pyplot as plt


def plot_profile(x, z, color="r", title=None, output=None):
    plt.figure()
    plt.plot(x,z, color)
    plt.xlabel("X")
    plt.ylabel("z")
    if title is not None:
        plt.title(title)
    if output is not None:
        plt.savefig(output)


def calculate_stable_time_step(dx, diffusivity):
    return 0.5* dx**2 / diffusivity


D= 100 # diffusivity
Lx = 300 # model domain

dx= 0.5 # grid spacing
x = np.arange(start=0, stop=Lx, step=dx) # the grid
nx= len(x) # number of grid nodes

z= np.zeros_like(x) # elevation
z_left= 300
z_right= 0
z[x<= Lx/2] = z_left # step
z[x> Lx/2] = z_right

plot_profile(x,z, title="Intial Profile", output="intial.png")

nt= 5000 # number of time steps
dt= calculate_stable_time_step(dx, D)

for t in range(0, nt):
	z[1:-1] += D * dt / dx ** 2 * (z[:-2] - 2*z[1:-1] + z[2:])

plot_profile(x,z, title="Final Profile", color="b", output="final.png")


