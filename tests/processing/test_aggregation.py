import pytest
from mlpipeline.processing.aggregation import create_new_col


def test_create_new_col():
    '''
    to test create_new_col() function
    '''

    aggs = {'height': ['max', 'min'], 'weight': ['sum']}
    output = create_new_col(aggs)
    expected_output = ['height_max', 'height_min', 'weight_sum']

    assert output == expected_output
