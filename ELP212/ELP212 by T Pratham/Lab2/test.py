import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

theta = np.array([np.pi*x/18 for x in range(37)])
h_power = [
    -28.31,
    -31.53,
    -33.47,
    -33.5,
    -35.5,
    -35.7,
    -39.5,
    -39.73,
    -40,
    -36.41,
    -33.56,
    -33.16,
    -39.04,
    -36.2,
    -34.7,
    -33.53,
    -30.53,
    -29.04,
    -27.14,
    -26.35,
    -25.72,
    -24.49,
    -25.57,
    -25.92,
    -26.75,
    -29.65,
    -32.5,
    -39.24,
    -31.88,
    -24.91,
    -23.25,
    -24.32,
    -25.74,
    -26.49,
    -28.17,
    -28.24,
    -28.31,
]

e_power = [
    -33.61,
    -32.75,
    -32.14,
    -33.35,
    -33.04,
    -34.88,
    -35.84,
    -35.74,
    -32.75,
    -30.68,
    -29.86,
    -28.77,
    -30.43,
    -34.44,
    -37.17,
    -40.87,
    -43.49,
    -42.01,
    -39.03,
    -39.33,
    -36.43,
    -32.04,
    -31.99,
    -27.35,
    -26.33,
    -28.68,
    -28.71,
    -30.03,
    -34.13,
    -39.11,
    -39.91,
    -40.34,
    -34.11,
    -35.12,
    -35.02,
    -37.06,
    -33.61
]
h_power = np.array(h_power)
e_power = np.array(e_power)

fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
# ax.set_rmax(100)

# for i in range(len(theta)-1):
    # plt.arrow(np.pi*theta[i]/180, h_power[i], np.pi*(theta[i+1]-theta[i])/180, h_power[i+1]-h_power[i])
ax.plot(theta, h_power, label='H-plane')
ax.plot(theta, e_power, label='E-plane')
# ax.set_rmax(-40)
# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width , box.height])
ax.set_rticks([r*ax.get_rmax()*2 for r in [0.5, 0.6, 0.7, 0.8, 1]])
plt.legend(loc='upper left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Angle (degrees)')
rlab = plt.ylabel("Power (dBm)")
rlab.set_position((0.0, 0.8))
rlab.set_rotation(0)
ax.yaxis.labelpad = -275
# plt.polar(theta, h_power, 'o')
# plt.polar(theta, e_power)
# plt.show()
plt.savefig('plot.png', dpi=300)