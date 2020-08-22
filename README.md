# freqit
Better frequency and crosstab tables.

This is a work in progress meant to provide better functionality and more options in constructing frequency tables for data analysis. Currently one-way tables are supported, crosstabulation tables to come in the future.

The package takes a pandas series and outputs a frequency table for the values within the column. 

Freqit requires that pandas and numpy are installed in the operating environment.

Installation:
pip install freqit

Use:
import freqit   
import pandas as pd

iris = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv')

freqit.oneway(iris['species']).freqtable()
