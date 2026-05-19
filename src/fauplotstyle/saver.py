import matplotlib.pyplot as plt

from typing import Literal
from uuid import uuid4
from datetime import datetime
from pathlib import Path

def save_figure(
    fig: plt.Figure,
    dirname: Path,
    filename: str=None,
    add_timestamp: bool = False,
    expand_figure: bool = True,
    fig_shape: Literal[
        "regular",
        "half-y",
        "half-x",
        "half-size",
        "page-wide",
        "double-size",
        "double-y",
        "nice-y",
    ] = "regular",
):
    if filename is None:
        filename = str(uuid4())
    if add_timestamp:
        ts = datetime.today().strftime(r"%Y_%m_%d_%H_%M_%S")
        filename = filename + ts
    
    figure_fpath= Path(dirname,filename + ".pdf")
    # saving the figure
    # the figure needs to be saved after the data as sometimes
    # one gets a TypeError from a faulty cache
    # since you can't pickle a _io.BufferedWriter
    bbox_inches = None
    figsize = plt.rcParams["figure.figsize"]
    if expand_figure:
        bbox_inches = "tight"

    # a full figure fits snugly in a revtex column
    michael_scaling = True
    subplot_row_scaling = True
    if michael_scaling:
        figsize = (figsize[0], figsize[1] * 1.5)
    if subplot_row_scaling:
        gridspec = fig.get_axes()[0].get_gridspec()
        figsize = (figsize[0], figsize[1] * gridspec.nrows / 2)
    if fig_shape == "regular":
        pass
    elif fig_shape == "half-y":
        figsize = (figsize[0], figsize[1] / 2)
    elif fig_shape == "double-y":
        figsize = (figsize[0], figsize[1] * 2)
    elif fig_shape == "nice-y":
        figsize = (figsize[0], figsize[1] * 1.5)
    elif fig_shape == "half-x":
        figsize = (figsize[0] / 2, figsize[1])
    elif fig_shape == "half-size":
        figsize = (figsize[0] / 2, figsize[1] / 2)
    elif fig_shape == "page-wide":
        figsize = (figsize[0] * 2, figsize[1])
    elif fig_shape == "double-size":
        figsize = (figsize[0] * 2, figsize[1] * 2)
    fig.set_size_inches(figsize[0], figsize[1])
    fig.savefig(figure_fpath , format="pdf", bbox_inches=bbox_inches, pad_inches=0.01)
    print("saved figure to {}".format(figure_fpath))
