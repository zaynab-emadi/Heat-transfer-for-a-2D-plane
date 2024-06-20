import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
start_time = time.time()
# Defining our problem
width = 0.3
height = 0.4
a = 0.25
delta = 0.01
initial_temp = 100
heat_flux = 500
iteration = 20000

node_x = int((width + delta) / delta) + 1
node_y = int((height + delta) / delta) + 1

u = np.full((node_y, node_x), initial_temp)   # plat is initially at 100 degrees c

# boundary condition
u[0, :] = 100
u[:, 0] = (heat_flux * 2 * delta - u[:, 2] + 4 * u[:, 1])/3
u[-1, :] = u[-2, :]
u[:, -1] = u[:, -2]


# simulating
counter = 0

while counter < iteration:
    u[:, 0] = (heat_flux * 2 * delta - u[:, 2] + 4 * u[:, 1]) / 3
    u[-1, :] = u[-2, :]
    u[:, -1] = u[:, -2]
    for i in range(1, node_y - 1):
        for j in range(1, node_x - 1):
            u[i, j] = u[i, j] + a * (u[i + 1, j] - 4 * u[i, j] + u[i - 1, j] + u[i, j + 1] + u[i, j - 1])
    counter += 1

print(pd.DataFrame(u))

x = np.linspace(height, 0, node_y - 2)
y = np.linspace(0, width, node_x - 2)
X, Y = np.meshgrid(x, y)
Z = u[1:-1, 1:-1]
# plt.contourf(Y, X, u.T, cmap=plt.cm.jet)
plt.pcolormesh(Y, X, Z.T, cmap=plt.cm.jet)
plt.title("Temperature")
plt.colorbar()
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))
print("finish")
