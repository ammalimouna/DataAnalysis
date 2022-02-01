import csv

filename = 'data2.csv'
filenamefields = 'fields.csv'

  
# initializing the titles and rows list
fields = []
fields1 = []
textfields = []
# fields =["very conservative"	"conservative"	"moderate"	"liberal"	"veryliberal"	"great deal"	"fair amount"	"not very much"	"none at all"	"The new york times"	"The wall street journal"	"USA Today"	"The washington post", "Fox News"	"Breitbart"	"CNN"	"Buzzfeed news"	"Huffington post"	"Time"	"U.S.News & World Report"	"yes"	"no"	"Decrease trust"	"Increase trust"	"no change"	"strongly approve"	"somewhat approve"	"somewhat disapprove"	"strongly disapprove"	"18-29"	"30-44"	"45-59"	"60+"	"female"	"male"	"$0 to $9.999"	"$10.000 to $24.999"	"$25.000 to $49.999"	"$50.000 to $74.999"	"$75.000 to $99.999"	"$100.000 to $124.999"	$100.000 to $124.999	"$150.000 to $174.999"	"$175.000 to $199.999"	"$200.000 and up"	"Prefer not to answer"	"New England"	"Middle Atlantic"	"East North Central"	"West North Central"	"South Atlantic"	"East South Central"	West South Central	Mountain	Pacific	iOS Phone / Tablet	Android Phone / Tablet	Other Phone / Tablet	Windows Desktop / Laptop	MacOS Desktop / Laptop	Other Phone / Tablet]

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
  
#  printing first 5 rows
print('\n\n')
for row in rows:
            length = len(row) 
            i = 0
            while i < length:
                if 9 <= i <= 19:
                    bool = False
                    while bool == False:
                        if row[i] == '1':
                            bool = True
                            new.append(textfields[i])
                        else :    
                            i += 1
                 
                    i = 20        
                else:                            
                    if row[i] == '1':
                            new.append(textfields[i])
                    i += 1        
            write.append(new)
            new = []
#new
print(len(rows[100]))
print(len(write))
filename1 = "outputv.csv"
with open(filename1, 'w' , newline='') as csvfile1:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile1)
      
    # writing the fields
    csvwriter.writerow(textfields)
      
    # writing the data rows
    csvwriter.writerows(write)




          