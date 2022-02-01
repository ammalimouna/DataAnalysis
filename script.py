import csv

filename = 'datasetcleaned.csv'
filenamefields = 'fields.csv'

  
# initializing the titles and rows list
fields = []
fields1 = []
textfields = []

rows = []
new = []
write = []

with open(filenamefields, 'r') as csvfile:
    # creating a csv reader object
    csvfieldsreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields1 = next(csvfieldsreader)
    textfields = next(csvfieldsreader)
  
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
print('\n')
print(textfields)
  
#  Mapping binary rows to text
print('\n\n')
for row in rows:
            length = len(row) - 6
            i = 0
            while i < length:
                # removing duplicate outlets to keep the first one 
                if 9 <= i <= 19:
                    bool = False
                    while bool == False:
                        if row[i] == '1':
                            bool = True
                            #adding selected fields to list 
                            new.append(textfields[i])
                        else :    
                            i += 1
                 
                    i = 20        
                else:                            
                    if row[i] == '1':
                            new.append(textfields[i])
                    i += 1  
            #adding list to global list      
            write.append(new)
            new = []
#new
print(len(rows[100]))
print(len(write))

#writing to new csv
filename1 = "outputWoDeviceCleaned.csv"
with open(filename1, 'w' , newline='') as csvfile1:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile1)
      
    # writing the fields
    csvwriter.writerow(textfields)
      
    # writing the data rows
    csvwriter.writerows(write)




          