import matplotlib.pyplot as plt
import numpy as np

rep = "yes"
while rep == "yes":
    print("To calculate vector addition\ntype v1 coordinate for example:2 3")
    while True:
        try:
            vx, vy = input("Vector 1:").split()
            try:
                vx = int(vx)
                vy = int(vy)
                break
            except ValueError or NameError:
                print("The entered number is in the wrong form, try to use the correct form:2 3")

        except ValueError or NameError:
            print('The entered number is in the wrong form, try to use the correct form:2 3')
    v1 = [vx, vy]

    while True:
        try:
            v2x, v2y = input("Vector 2:").split()
            try:
                v2x = int(v2x)
                v2y = int(v2y)
                break
            except ValueError or NameError:
                print("The entered number is in the wrong form, try to use the correct form:2 3")

        except ValueError or NameError:
            print('The entered number is in the wrong form, try to use the correct form:2 3')
    v2 = [v2x, v2y]

    sum1 = vx + v2x
    sum2 = vy + v2y
    r = [sum1, sum2]
    magnitude = np.linalg.norm(r)
    magnitude = round(magnitude, 2)
    origin = [0, 0]

    fig, ax = plt.subplots()
    ax.set_xlim(-1, sum1 + 3)
    ax.set_ylim(-1, sum2 + 3)
    plt.ylabel("Y axis")
    plt.xlabel("X axis")

    ax.quiver(origin[0], origin[1], v1[0], v1[1], angles="xy", scale_units="xy", scale=1, color="b", label=f"V1 = {v1}")
    ax.quiver(v1[0], v1[1], v2[0], v2[1], angles="xy", scale_units="xy", scale=1, color="g", label=f"V2 = {v2}")
    ax.quiver(origin[0], origin[1], r[0], r[1], angles="xy", scale_units="xy", scale=1, color="r", label=f"V3 = {r}\nLength={magnitude}")
    plt.legend()
    plt.show()
    plt. close("all")
    while True:
        rep = input("Do you want to add another vector?\nType(yes/no):")
        if rep == "no" or rep == "yes":
            break
        else:
            print("Input error")