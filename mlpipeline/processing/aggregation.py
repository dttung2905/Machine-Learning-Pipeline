import pandas as pd


def create_new_col(aggs: dict) -> list:
    '''
    Create a list of new column name from the config
    Eg : {'height': ['max','min'], 'weight': 'sum'}
    --> ['height_max', 'height_min', 'weight_sum']
    '''
    return [k + "_" + v for k in aggs for v in aggs[k]]


def custom_aggregation(
            df: pd.DataFrame, agg_col: str, config: dict) -> pd.DataFrame:
    '''
    This function helps to perform automatic aggregation functions for
    specific column in pandas dataframe

    Args:
        - df : input dataframe
        - agg_col : column to perform aggregation on
        - config : the dictionary for custom metric
            - key : column name
            - value: metrics (can be a list)
        Eg: {'colunmA':['mean','max'],'columnB':'min'}
    Output:
        - result pandas Dataframe with corresponding metrics per column
    '''

    df_agg = df.groupby(agg_col).agg(config)
    df_agg.columns = create_new_col(config)
    df_agg.reset_index(inplace=True)

    return df_agg
