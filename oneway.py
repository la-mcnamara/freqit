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

    def freqtable(self, sort='value', ): 
        """
        One-way frequency table.

        sort: value (default), number, or pct
        """

        table = (pd.concat([self.series.value_counts().rename('count'), 
                self.series.value_counts(normalize=True).mul(100).rename('percentage')], 
                axis=1)
                .reset_index()
                .rename(columns={'index': 'value'}))
        
        if sort in ['value','count','pct','percentage']:
            if sort == 'pct':
                sort = 'percentage'
            
            table = table.sort_values(by=[sort])
        else: 
            print('Invalid sort!')
 
        totn = table['count'].sum()

        table = (pd.concat([table,
                          table['count'].cumsum().rename('cum_total'),
                          table['count'].cumsum().div(totn).mul(100).rename('cum_percentage')], 
                          axis=1).reset_index(drop=True)
                          )

        return table
        
        # return self.series.value_counts()
        
