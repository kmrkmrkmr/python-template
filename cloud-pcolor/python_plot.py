import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath} \usepackage{amsfonts} 
   \usepackage{amssymb} \usepackage{bm}''')
rc('font',**{'family':'serif','serif':['Times'],'size':10})


# Create a grid of x, y values
x = np.linspace(0, 10, 100)
y = np.linspace(0, 5, 50)

# Create a 2D array of z values (some function of x and y)
x, y = np.meshgrid(x, y)
z = np.sin(x) + np.cos(y)

# Set the size in centimeters
fig_width_cm, fig_height_cm = 7.32, 5.49

# Convert centimeters to inches
cm_to_inches = 0.393701
fig_width = fig_width_cm * cm_to_inches
fig_height = fig_height_cm * cm_to_inches

# Create a new figure and set size
plt.figure(figsize=(fig_width, fig_height))

# Create a pseudocolor plot
plt.pcolor(x, y, z, shading='auto', cmap='viridis')

# Add colorbar
# plt.colorbar(label=r'$\bm{Z}$\textbf{-values}')

cbar = plt.colorbar()
cbar.ax.set_title(r'\textbf{Z Value}')

# Add labels with custom font and adjust labelpad
plt.xlabel(r'\textbf{Time (s)}', labelpad=0)  # Set labelpad to 0
plt.ylabel(r'\textbf{Displacement (m)}', labelpad=0)  # Set labelpad to 0

# Get the current axis
ax = plt.gca()

# Set ticks inside the plot
ax.tick_params(axis='both', which='both', direction='in', 
               bottom=True, top=True, left=True, right=True)

# # Set the axis range
# plt.xlim(0, 10)

# # Set the y-axis limits explicitly
# plt.ylim(0, 0.1)

# Set font for tick labels
# ax.set_xticks(ax.get_xticks())
# ax.set_xticklabels(ax.get_xticks(), fontsize=10, fontfamily='Times New Roman')

# ax.set_yticks(ax.get_yticks())
# ax.set_yticklabels(ax.get_yticks(), fontsize=10, fontfamily='Times New Roman')

# Set the axis range
plt.xlim(0, 10)

# Set the y-axis limits explicitly
plt.ylim(0, 5)

# Add dashed grid
#ax.grid(linestyle='--', linewidth=0.5)

# used if you want to set the whole size of figure
#plt.tight_layout()

# Save the figure as a PNG
plt.savefig('plot.png', bbox_inches='tight', dpi=300)

# Show the plot
plt.show()

