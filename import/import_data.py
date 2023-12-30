import numpy as np

# import txt data
file_path = 'point1.txt'
data_txt = np.loadtxt(file_path, delimiter='\t', skiprows=0)

# import csv data
file_path = 'time.csv'
data_csv1 = np.genfromtxt(file_path, delimiter=',', skip_header=0)
file_path = 'generalized_node_position.csv'
data_csv2 = np.genfromtxt(file_path, delimiter=',', skip_header=0)