import pandas as pd
import numpy as np

class xtab:
    """ A class used to represent a crosstabulation table

    Attributes
    ----------
    df : pandas DataFrame
        A DataFrame with source data for computing crosstabs
    cols : list
        A list of columns to compute crosstab on
    sort : str, optional
        The column the frequency table should be sorted on - 
        value (series data), count (count of values), or pct
        (percentage of values).
        default = value
    asc : bool, optional
        Flag indicating if sort should be ascending.
        default = True

    Methods
    -------
    freqtable()
        Multi-variable frequency table.
    """

    def __init__(self, df, cols, sort='value', asc=True):
        """ Constructor for this class. """ 
        self.df = df
        self.cols = cols
        self.sort = sort
        self.asc = asc
    
    def freqtable(self):
        # summing
        ct = df.groupby([cols])  \
                    .size()         \
                    .rename(columns={0:'count'})    

        return ct