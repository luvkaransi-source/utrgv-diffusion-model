#!/usr/bin/env python
# coding: utf-8

# # A 1D diffusion model

# ## Here we develop a 1D numerical model

# Here we have diffusion eq
# $$ \frac{\partial z}{\partial t} = D\frac{\partial^2 z}{\partial x^2} $$

# here $z$ is elevation, $x$ is spatial dimension, and $D$ is transport rate coefficient (or diffusivity).

# The discretized version of this eq is: 
# $$ z^{t+1}_x = z^t_x + {D \Delta t \over \Delta x^2} (z^t_{x+1} - 2z^t_x + z^t_{x-1}) $$
# This is the FTCS scheme for solving the diffusion eq.

# We'll use two Python libraries, NumPy (for arrays) amd Mataplotlib (for plotting), that aren't a part of the core Python library.

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# Start by setting two fixed model parameters, the diffusivity anda the size off the model domain.

# In[ ]:


D= 100 # diffusivity
Lx = 300 # model domain


# Next, set up the model grid using NumPy array

# In[ ]:


dx= 0.5 # grid spacing
x = np.arange(start=0, stop=Lx, step=dx) # the grid
nx= len(x) # number of grid nodes


# Set the initial conditions fo the model.
# The elevation $z$ is a step function with a high value on the left, a low value on the right, and a cliff on the center of the domain.

# In[ ]:


z= np.zeros_like(x) # elevation
z_left= 300
z_right= 0
z[x<= Lx/2] = z_left # step
z[x> Lx/2] = z_right


# Make a plot of initial conditions of the model.

# In[ ]:


plt.figure()
plt.plot(x,z, "r")
plt.xlabel("X")
plt.ylabel("z")
plt.title("Initial profile")


# Set the number of time steps in the model.
# Caclculate a stable time step using a stability criterion.

# In[ ]:


nt= 5000 # number of time steps
dt= 0.5 * dx**2 / D # time step


# Loop over the time of the model, solving the diffusion eq using the FTCS scheme described above.

# In[ ]:


for t in range(0, nt):
	z[1:-1] += D * dt / dx ** 2 * (z[:-2] - 2*z[1:-1] + z[2:])


# Note that this is an array operation on the elevation $z$.
# The boundary conditions remain fixed in each time step.

# Plot the result of running the model.

# In[ ]:


plt.figure()
plt.plot(x,z, "b")
plt.xlabel("X")
plt.ylabel("z")
plt.title("Final profile")


# In[ ]:




