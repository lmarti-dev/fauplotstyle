import matplotlib.pyplot as plt

import numpy as np

import fauplotstyle


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols=2, nrows=2)
axes = (ax1, ax2, ax3, ax4)
for ax in axes:
    for uu in range(np.random.randint(1, 7)):
        x = sorted(np.random.rand(100))
        y = sorted(np.random.rand(100))
        ax.plot(x, y, label=uu)
    ax.legend()
    ax.set_xlabel("X-label")
    ax.set_ylabel("Y-label")

fig.suptitle("Suptitle")
fig.tight_layout()
plt.show()
