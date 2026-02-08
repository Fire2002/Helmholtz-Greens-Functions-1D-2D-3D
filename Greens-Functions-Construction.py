# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 08:31:44 2024

@author: Fire2002
"""

# This code defines eigenfunction expansions for the Green's functions of the Helmholtz equation in 1D, 2D, and 3D.

import numpy as np
import matplotlib.pyplot as plt

def green_function_1D(x, x0, k, L, pts=10): # fxn to calc in 1D
    res = 0
    for n in range(1, pts+1):
        eigenvalue = (n * np.pi / L)**2 - k**2
        if eigenvalue != 0:
            res += np.sin(n * np.pi * x / L) * np.sin(n * np.pi * x0 / L) / eigenvalue
    return res

def green_function_2D(x, y, x0, y0, k, L, pts=50): # fxn to calc in 2D
    res = 0
    for nx in range(1, pts+1):
        for ny in range(1, pts+1):
            eigenvalue = ((nx * np.pi / L)**2 + (ny * np.pi / L)**2) - k**2
            if eigenvalue != 0:
                res += (np.sin(nx * np.pi * x / L) * np.sin(ny * np.pi * y / L) *
                           np.sin(nx * np.pi * x0 / L) * np.sin(ny * np.pi * y0 / L)) / eigenvalue
    return res

def green_function_3D(x, y, z, x0, y0, z0, k, L, pts=5): # fxn to calc in 3D
    res = 0
    for nx in range(1, pts+1):
        for ny in range(1, pts+1):
            for nz in range(1, pts+1):
                eigenvalue = ((nx * np.pi / L)**2 + (ny * np.pi / L)**2
                              + (nz * np.pi / L)**2) - k**2
                if eigenvalue != 0:
                    res += (np.sin(nx * np.pi * x / L) * np.sin(ny * np.pi * y / L) *
                            np.sin(nz * np.pi * z / L) * np.sin(nx * np.pi * x0 / L) *
                               np.sin(ny * np.pi * y0 / L) * np.sin(nz * np.pi * z0 / L)) / eigenvalue
    return res

L = 1
x_values = np.linspace(0, L, 100)
y_values = np.linspace(0, L, 100)
z_values = np.linspace(0, L, 100)
x0 = y0 = z0 = L/2 # source point
plt.figure(figsize=(15, 5))

def plot_1D():
    green_1D = green_function_1D(x_values, x0, np.pi / L, L)
    plt.subplot(131)
    plt.plot(x_values, green_1D)
    plt.title('Green\'s function in 1D')
    plt.show()

def plot_2D():
    green_2D = green_function_2D(x_values[:, np.newaxis], y_values, x0, y0, np.pi / L, L)   
    plt.subplot(132)
    plt.imshow(green_2D, extent=[0, L, 0, L], origin='lower', cmap='viridis')
    plt.title('Green\'s function in 2D')
    plt.show()

def plot_3D():
    green_3D = green_function_3D(x_values[:, np.newaxis, np.newaxis], y_values[np.newaxis, :, np.newaxis], z_values[np.newaxis, np.newaxis, :], x0, y0, z0, np.pi / L, L)    
    plt.subplot(133)
    plt.imshow(green_3D[:, :, int(len(z_values) / 2)], extent=[0, L, 0, L], origin='lower', cmap='viridis')
    plt.title('Green\'s function in 3D (slice)')
    plt.show()

plot_1D()
plot_2D()
plot_3D()





















