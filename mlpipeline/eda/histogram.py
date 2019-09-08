import pandas as pd
import matplotlib.pyplot as plt


def overlap_hist(series_1: pd.core.series.Series,
                 series_2: pd.core.series.Series,
                 label_1: str, label_2: str, location: str = 'upper_right'):
    """
    This function will create an overlapped historgram
    Args:
        series_1: first pandas series to be plotted
        series_2: second pandas series to be plotted
        label_1: label of the first pandas series in legend
        label_2: label of the second pandas series in legend
        location: location of the legend
    Return:
        figure with plot
    """
    avail_position = ["upper right", "upper left", "lower left",
                      "lower right", "right", "center left", "center right",
                      "lower center", "upper center", "center"]
    if location not in avail_position:
        raise Exception("[{}] not in available position {}".format(
                                                                location,
                                                                avail_position))
    fig = plt.figure()
    plt.hist(series_1, alpha=0.5, label=label_1)
    plt.hist(series_2, alpha=0.5, label=label_2)
    plt.legend(loc=location)
    plt.show()
    return fig
