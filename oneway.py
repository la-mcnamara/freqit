import pandas as pd

class oneway:

    def __init__(self, series):
        """ Constructor for this class. """ 
        self.series = series
    
    def justprint(self): 
        """
        Just print a variable name
        """
        print(self.name)

    def freqtable(self, sort='value'): 
        """
        One-way frequency table.
        sort: value (default), number, or pct
        """

        table = (pd.concat([self.series.value_counts().rename('count'), 
                self.series.value_counts(normalize=True).mul(100).rename('percentage'),
                self.series.value_counts().cumsum().rename('cum_total'),
                self.series.value_counts(normalize=True).cumsum().mul(100).rename('cum_percentage')], axis=1)
                .reset_index()
                .rename(columns={'index': 'value'}))
        
        if sort in ['value','count','pct','percentage']:
            if sort == 'pct':
                sort = 'percentage'
            
            table = table.sort_values(by=[sort])
        else: 
            print('Invalid sort!')

        return table
        
        # return self.series.value_counts()
        
