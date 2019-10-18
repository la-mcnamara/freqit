class oneway:
    def __init__(self, series):
        """ Constructor for this class. """ 
        self.series = series
    
    def justprint(self): 
        """
        Just print a variable name
        """
        # print('Var is ', var)
        print(self.name)

    def freqtable(self): 
        """
        One-way frequency table.
        """

        # return (pd.concat([df[var].value_counts().rename('number'), 
        #         df[var].value_counts(normalize=True).mul(100).rename('percentage'),
        #         df[var].value_counts().cumsum().rename('cum_total'),
        #         df[var].value_counts(normalize=True).cumsum().mul(100).rename('cum_percentage')], axis=1)
        #         .reset_index()
        #         .rename(columns={'index': 'value'}))
        
        return self.series.value_counts()
        
