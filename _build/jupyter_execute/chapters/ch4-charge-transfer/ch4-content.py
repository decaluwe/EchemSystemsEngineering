#!/usr/bin/env python
# coding: utf-8

# # Chapter 4: Charge Transfer Kinetics

# Let's consider the charge-transfer reaction at the PEMFC anode:
# 
# $${\rm H_{Pt(s)}  \leftrightharpoons H^+_{elyte} + e^-_{Pt}}$$
# 
# Calculate current as a function of overpotential at 50$^\circ$ C, using the Butler-Volmer approximation and assuming a constant exchange current density of $i_\circ = 2.15$ A/cm$^2$. Assume a symmetry factor of 0.5.

# In[1]:


import numpy as np
from math import exp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

etas = np.concatenate([np.geomspace(-.25, -1e-3, 50), np.geomspace(1e-3, .25, 50)])
currents = np.zeros_like(etas)

# Constants:
R = 8.3145 # J/mol-K
F = 96485  # C per mol e-

# Inputs
i_0 = 2.15 # Exchange current density, A/cm2
n = 1      # Elementary charge transferred
T = 298.15 # K
alpha_f = 0.5


for i, eta in enumerate(etas):
    currents[i] = 


# In[ ]:


plt.semilogy(etas, abs(currents), 'ro')
plt.ylabel('Current (A/cm$^2$)', fontsize=16)
plt.xlabel('Overpotential (V)', fontsize=16)


# In[ ]:




