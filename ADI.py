import numpy as np
import matplotlib as plt
import pandas as pd

width = 0.3
height = 0.4
a = 0.25
delta = 0.01
initial_temp = 100
heat_flux = 500
iteration = 20000

node_x = int((width + delta) / delta) + 1
node_y = int((height + delta) / delta) + 1

