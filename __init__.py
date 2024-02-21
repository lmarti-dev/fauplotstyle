import os
from matplotlib import font_manager
import matplotlib.pyplot as plt

HOME = os.path.dirname(__file__)

font_path = os.path.join(
    HOME, "fonts/Roboto/Roboto-Regular.ttf"
)  # Your font path goes here
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = prop.get_name()

plt.style.use(os.path.join(HOME, "styles/default_new_style.mplstyle"))


# keys can be found at:
# https://matplotlib.org/stable/users/explain/customizing.html#the-default-matplotlibrc-file
