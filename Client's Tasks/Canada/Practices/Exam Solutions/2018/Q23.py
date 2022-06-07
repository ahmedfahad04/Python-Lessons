import numpy as np

def motionEquations(x0, v0, a, duration, intervals):
    time = np.linspace(0, duration, intervals)
    print(time)
    vf0 = v0 + a * time
    xf0 = x0 + v0 * time + (a * (time ** 2)) / 2
    vf1 = np.sqrt((v0 ** 2) + 2 * a * (xf0 - x0))
    xf1 = x0 + ((v0 + vf0) * time) / 2

    return vf0, vf1, xf0, xf1

# # NEVER INCLUDE these lines IN EXAM. Before submitting you must delete it.
# v0, v1, x0, x1 = motionEquations(2, 5, 3, 10, 5)
# for a,b,c,d in zip(v0,v1,x0,x1):
#     print("V0: ", a)
#     print("V1: ", b)
#     print("X0: ", c)
#     print("X1: ", d)
#     print()


