import matplotlib.pyplot as plt

import numpy as np

from fauplotstyle.styler import style


def test_default_plot4():
    style()
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(
        ncols=2, nrows=2, constrained_layout=True
    )
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

    plt.show()


def test_default_plot2():
    style()

    fig, (ax1, ax2) = plt.subplots(nrows=2, constrained_layout=True)
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
    plt.show()


def test_cmap_plot():
    """
    Helper function to plot data with associated colormap.
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)
    fig, ax = plt.subplots()
    cmap = plt.get_cmap("fau_cmap")
    psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
    fig.colorbar(psm, ax=ax)
    plt.show()


def test_error_bar_plot():
    np.random.seed(3132)
    data = np.random.rand(100)
    std = np.random.rand(100) / 10

    fig, ax = plt.subplots()
    ax.errorbar(range(len(data)), data, std)
    plt.show()


test_default_plot2()
test_default_plot4()
test_error_bar_plot()
test_cmap_plot()
