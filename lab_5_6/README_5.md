# DataFrame_Pandas
1 Read any data source into pandas DataFrame: CSV, JSON, Excel file, HTML table, embedded sklearn dataset. Describe your data, what each column means, what type (categorical, real, integer, binary) the column is, if necessary, decode the values for categorical and binary attributes. In general, perform a "visual" analysis of your data.

2 Do the following operations with dataframe (many operations can be done in more than one way, use all methods you know, look for/invent new ones) :

2.1 table output

2.2 output first 5 table elements

2.3 print the last 5 table entries

2.4 use describe() function

2.5 read value of a cell (with a certain index from a certain column) by all means you know

2.6 filtering rows by index range

2.7 data set filtering by any condition

2.8 work with missing values (if any): delete rows with missing values, fill missing values with the average value of the column. If there are no missing values - intentionally "generate" them by nailing some pieces of data to np.nan

2.9. Create a new field calculated on the basis of other fields' values:

2.9.1 via an expression based on existing columns,

2.9.2 via DataFrame.apply

2.9.3 via Series.apply

2.10 sorting by any of the fields

2.11 calculate several statistics by columns (use built-in aggregate functions - any you like)

2.12 .value_counts()

2.13 Output unique column values via .unique()

2.14 Delete the current index and create a new index based on the new column that works best for it
