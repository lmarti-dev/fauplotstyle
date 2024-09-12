import matplotlib.pyplot as plt

import numpy as np

from fauplotstyle.styler import style


def test_default_plot4():
    style()
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


def test_default_plot2():
    style()
    fig, (ax1, ax2) = plt.subplots(nrows=2)
    axes = (ax1, ax2)
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


def test_cmap_plot():
    """
    Helper function to plot data with associated colormap.
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)
    fig, ax = plt.subplots()
    cmap = plt.get_cmap("faucmap")
    psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
    fig.colorbar(psm, ax=ax)
    plt.show()


test_default_plot2()
test_cmap_plot()
