import panas as pd
import numpy as np

def drop_null(df , threshold = 0.5):
    
    """ Remove columns with the more than a cirtain percentage of values
    This will only delete a rows of a column if it is more than a percentage in the parameter given by you.
    Default valule is 0.5"""
    
    missing_percentage = df.isnull().mean()
    rows_to_drop = missing_percentage[missing_percentage > threshold].index
    
    return df.drop(rows= rows_to_drop)