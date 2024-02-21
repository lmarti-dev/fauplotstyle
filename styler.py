import os
from matplotlib import font_manager
import matplotlib.pyplot as plt

HOME = os.path.dirname(__file__)


def use_style(style_name: str = None):
    if style_name is None:
        style_name = "default_new_style"
    STYLES[style_name]()


def default_new_style():
    font_path = os.path.join(HOME, "fonts/Roboto/Roboto-Regular.ttf")
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)

    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = prop.get_name()

    plt.style.use(os.path.join(HOME, "styles/default_new_style.mplstyle"))


STYLES = {"default_new_style": default_new_style}


# keys can be found at:
# https://matplotlib.org/stable/users/explain/customizing.html#the-default-matplotlibrc-file
