import csv
infocsv = open('./info.csv',  encoding="utf-8") #파일이 있는 경로+파일이름.csv
value_csv1 = csv.reader(infocsv)
csv_info=[]
for value_csv2 in value_csv1 :
    csv_info.append(value_csv2)

#csvname = csv_info[0]
#csvbirthday = csv_info[1]
#csvpassword = csv_info[2]

a=str(csv_info[2])

print(a[2:3])
print(a[3:4])
print(a[4:5])
print(a[5:6])
