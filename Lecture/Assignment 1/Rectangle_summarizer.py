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

with open('rectangles_data.csv', newline="") as f:
        reader = csv.reader(f)
        next(reader) ## table of strings - next to not read header
        width_list = [] ## three empty lists to be appended to the values
        height_list = []
        area_list = []
        for row in reader: # for creates a loop
            width = float(row[1]) ## Float to tell the system the csv are numbers not strings
            height = float(row[2])
            width_list.append(width)
            height_list.append(height)
            area_list.append(width * height)
        # print(f'{max(area_list)}') ## this is to test
    ## create a data dictionary
        data = {
         'max': max(area_list),
         'min': min(area_list),
         'count': len(area_list),
         'average':st.mean(area_list),
         'total value': sum(area_list)
         }
        
        csv_file = "Summary_Results_Rectanglesf.csv"
        
        with open("Summary_Results_Rectanglesf.csv", 'w', newline="", encoding= 'utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data.keys())
            writer.writerow(data.values())



## print
#print(f'max={max(area_list)},\nmin={min(area_list)},\ncount={len(area_list)},\naverage={st.mean(area_list)}') 





#%%

            

        





#Stores the above information in another CSV file named summary.csv
# %%
