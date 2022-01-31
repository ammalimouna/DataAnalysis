import csv

filename = 'dataset.csv'

  
# initializing the titles and rows list
fields = [Very conservative , Very conservative ]
fields =['']
rows = []
new = []
write = []
  
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
    fields[0] = 'A1'
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
print(fields)
  
#  printing first 5 rows
print('\n\n')
for row in rows:
        for i in range(len(row)):
            if row[i] == '1':
                new.append(fields[i])
        write.append(new)
        new = []
#new
print(rows[0])
print(len(write))
filename1 = "output.csv"
with open(filename1, 'w') as csvfile1:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile1)
      
    # writing the fields
    csvwriter.writerow(fields)
      
    # writing the data rows
    csvwriter.writerows(write)




          