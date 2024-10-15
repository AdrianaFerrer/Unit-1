#Reads the content of a CSV file
#Counts and prints out the total count of rectangles
#%%
import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)  ##skip headings
    for row in reader:
        print(row)
       
        
#%% 
total_rows = 0
import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total_rows += 1
print(f'Total number of count: {total_rows}') #PRINT COUNTS

#%%
#PRINT MIN AND MAX
#%%

import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)  ##skip headings
    for row in reader:
        print(min(reader))
        print(max(reader))

#%%

import math
import statistics as st
import csv
def calculate_total_area(rectangles_data.csv):

    with open('rectangles_data.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
                width = float(row[1])
                lenght = float(row[2])

                area = width * lenght
                total_area = sum(area)
    
            

        





#Stores the above information in another CSV file named summary.csv
# %%
