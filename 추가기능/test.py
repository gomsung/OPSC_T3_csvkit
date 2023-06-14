import csv
# Extract headers
file = open('test.csv',  encoding='utf-8-sig')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
#print(header)

#Extract Rows
rows = []
for row in csvreader:
    rows.append(row)


#Keyword Filtering --> 행수/키워드 

def keywordFiltering(colNum, keyword):
    userName = []
    for i in range(0,len(rows)):
        if rows[i][colNum] == keyword:
            userName.append(rows[i][0])
    return userName

result = keywordFiltering(2, "23")

print("Print all users' names: ", result)
