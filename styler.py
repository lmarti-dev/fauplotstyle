import os
from matplotlib import font_manager, colormaps
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import ColormapRegistry
import matplotlib.pyplot as plt


HOME = os.path.dirname(__file__)


def style(style_name: str = None):
    if style_name is None:
        style_name = "default_new_style"
    STYLES[style_name]()
    add_fau_cmap()


def set_default_font():
    font_path = os.path.join(HOME, "fonts/Roboto/Roboto-Regular.ttf")
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)

    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = prop.get_name()


def default_new_style():

    plt.style.use(os.path.join(HOME, "styles/default_new_style.mplstyle"))


def add_fau_cmap():
    colors = [
        "#228848",
        "#0061A0",
        "#AAC3D1",
        "#971B2F",
    ]
    fau_cmap = LinearSegmentedColormap.from_list("fau_cmap", colors)

    # can't register a colormap twice
    if "fau_cmap" in colormaps:
        pass
    else:
        colormaps.register(cmap=fau_cmap)


STYLES = {"default_new_style": default_new_style}


# keys can be found at:
# https://matplotlib.org/stable/users/explain/customizing.html#the-default-matplotlibrc-file
