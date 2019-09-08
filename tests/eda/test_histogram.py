import pytest
import matplotlib.pyplot as plt
from mlpipeline.eda.histogram import overlap_hist
import pandas as pd
import os


#@pytest.mark.mpl_image_compare(baseline_dir='. ', filename='overlap_hist.png')
@pytest.mark.mpl_image_compare
def test_overlap_hist():
    print("*********")
    print(os.getcwd())
    df = pd.read_csv('dataset/Auto.csv')
    df.head()
    df['horsepower'].replace("?", 0, inplace=True)
    df['horsepower'] = df['horsepower'].astype(int)
    with pytest.raises(Exception) as excinfo:
        overlap_hist(
                           df[df['origin'] == 1]['horsepower'],
                           df[df['origin'] == 2]['horsepower'],
                           'x',
                           'y',
                           'random place')
    assert "[random place] not in available position ['upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center']" in str(excinfo.value)
    output_fig = overlap_hist(
                       df[df['origin'] == 1]['horsepower'],
                       df[df['origin'] == 2]['horsepower'],
                       'x',
                       'y',
                       'upper right')

    return output_fig

