# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 12:39:18 2025

@author: VK
"""

import numpy as np

# Given parameters
Ti = 85.0       # inner temperature (C)
To = 0.0        # outside temperature (C)
hi = 125.0      # inner heat transfer coefficient (W/m2K)
ho =10.0        # outer heat transfer coefficient (W/m2K)
k_pipe = 45.0   # pipe wall conductivity (W/mK)
k_ins = 0.1     # insulation conductivity (W/mK)

# Geometry (m)
D_i = 0.095   # inner diameter (m)
t_pipe = 0.0225

r_i = D_i/2                    # inner radius
r_pipe_o = r_i + t_pipe        # outer radius of pipe wall

# insulation
th_ins = 0.1
r_ins_o = r_pipe_o + th_ins    # outer radius with insulation

# Length (per meter)
L = 1.0

# Thermal resistances per unit length
R_conv_i = 1.0 / (hi * 2 * np.pi * r_i * L)
R_pipe = np.log(r_pipe_o/r_i) / (2 * np.pi * k_pipe * L)
R_ins = np.log(r_ins_o/r_pipe_o) / (2 * np.pi * k_ins * L)
R_conv_o = 1.0 / (ho * 2 * np.pi * r_ins_o * L)

R_total = R_conv_i + R_pipe + R_ins + R_conv_o

# Heat loss per unit length (W/m)
q_prime = (Ti - To) / R_total

print(f"Total thermal resistance per meter: {R_total:.6f} K/W")
print(f"Heat loss per meter of pipe: {q_prime:.2f} W/m")
