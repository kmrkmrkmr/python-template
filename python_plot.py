import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath} \usepackage{amsfonts} 
   \usepackage{amssymb} \usepackage{bm}''')
rc('font',**{'family':'serif','serif':['Times'],'size':10})

# import txt data
file_path = 'point1.txt'
data_txt = np.loadtxt(file_path, delimiter='\t', skiprows=0)

# import csv data
file_path = 'time.csv'
data_csv1 = np.genfromtxt(file_path, delimiter=',', skip_header=0)
file_path = 'generalized_node_position.csv'
data_csv2 = np.genfromtxt(file_path, delimiter=',', skip_header=0)


# Set the size in centimeters
fig_width_cm, fig_height_cm = 7.32, 5.49

# Convert centimeters to inches
cm_to_inches = 0.393701
fig_width = fig_width_cm * cm_to_inches
fig_height = fig_height_cm * cm_to_inches

# Create a new figure and set size
plt.figure(figsize=(fig_width, fig_height))

# Plot the data with labeled axes
plt.plot(data_txt[:,0], data_txt[:,1], label=r'txt data', color='blue', linestyle='-', linewidth=2)
plt.plot(data_csv1, data_csv2[:,0], label=r'csv data', color='red', linestyle='--', linewidth=2)

# Add labels with custom font and adjust labelpad
plt.xlabel(r'\textbf{Time (s)}', labelpad=0)  # Set labelpad to 0
plt.ylabel(r'\textbf{Displacement (m)}', labelpad=0)  # Set labelpad to 0

# Add a legend with custom font and a sharp black box
legend = plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), 
                    frameon=True, fancybox=False, edgecolor='black', 
                    handlelength=1.8, handletextpad=0.4)
legend.get_frame().set_alpha(1)

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
plt.ylim(0, 0.1)

# Add dashed grid
ax.grid(linestyle='--', linewidth=0.5)

# used if you want to set the whole size of figure
#plt.tight_layout()

# Save the figure as a PNG
plt.savefig('plot.png', bbox_inches='tight', dpi=300)

# Show the plot
plt.show()
