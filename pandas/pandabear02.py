#!/usr/bin/env python3

""" """

import pandas as pd

# these lines are forl writing to file
# use this when you are not rendering to a window
import matplotlib
matplotlib.use('Agg')

# create some graphs
import matplotlib.pyplot as plt

def main():
    #define our xls file
    excel_file = 'movies.xls'

    # choose the first column 'title' as
    # index (index=0)
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    # data frame has 5 rows and 24 columns (indexed by title)
    print(movies_sheet1.head())

    # grab the next two sheets as well
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    # data frame has 5 rows and 24 columns (indexed by title)
    print(movies_sheet2.head())

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    print(movies_sheet3.head())

    # combine all DFs into a single data frame called movies
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    # number of rows and columns (5042, 24)
    print(movies.shape)

    # unfortunately our data has some duplicates in it
    # we can remove them quickly with the .drop_duplicates() method
    # this returns a dataframe, or None if .drop_duplicates(inplace=True)
    movies.drop_duplicates(inplace=True)

    # take a peek at how our dataframe changed after removing duplicates
    print(movies.shape)

    # sort DataFrame based on Gross Earnings
    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    # Data is sorted by values in a column
    # display the top 10 movies by Gross Earnings.
    # passing the 10 values to head returns the top 10 not the default 5
    print(sorted_by_gross.head(10))

    # create a stacked bar graph
    sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")
    # save the figure as stackedbar.png
    plt.savefig("/home/student/static/stackedbar.png", bbox_inches='tight')

if __name__ == "__main__":
    main()
