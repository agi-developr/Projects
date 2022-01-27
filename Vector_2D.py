import matplotlib.pyplot as plt
v1 = [2, 3]
v2 = [0, 5]
r = [2, 8]
origin = [0, 0]

fig, ax = plt.subplots()

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 10)
ax.quiver(origin[0], origin[1], v1[0], v1[1], angles="xy", scale_units="xy", scale=1, color = "b")
ax.quiver(v1[0], v1[1], v2[0], v2[1], angles="xy", scale_units="xy", scale=1, color = "g")
ax.quiver(origin[0], origin[1], r[0], r[1], angles="xy", scale_units="xy", scale=1, color = "r")

plt.show()

a = np.array([1,2,3])
print(a)

b = np.array([[1,2,3],[6,5,4]])
print(b)