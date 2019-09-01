import pytest
from mlpipeline.processing.aggregation import \
        create_new_col, custom_aggregation
import pandas as pd
from pandas.util.testing import assert_frame_equal


def test_create_new_col():
    '''
    to test create_new_col() function
    '''

    aggs = {'height': ['max', 'min'], 'weight': ['sum']}
    output = create_new_col(aggs)
    expected_output = ['height_max', 'height_min', 'weight_sum']

    assert output == expected_output


def test_custom_aggregation():
    '''
    test the custom_aggregation() function
    '''
    input_df = {'colA': [1, 2, 3, 4],
                'colB': [3, 4, 2, 1],
                'colC': ['X', 'X', 'Y', 'Y']}
    input_df = pd.DataFrame(data=input_df)
    agg_col = 'colC'
    config = {'colA': ['mean', 'sum'], 'colB': ['max']}
    return_df = custom_aggregation(input_df, agg_col, config)
    expected_df = {'colC': ['X', 'Y'],
                   'colA_mean': [1.5, 3.5],
                   'colA_sum': [3, 7],
                   'colB_max': [4, 2]}
    expected_df = pd.DataFrame(data=expected_df)
    assert_frame_equal(expected_df, return_df)
