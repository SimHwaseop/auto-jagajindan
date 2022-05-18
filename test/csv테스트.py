import csv

testcsv = open('./test.csv',  encoding="utf-8") #파일이 있는 경로+파일이름.csv
value_csv1 = csv.reader(testcsv)
csv_value=[]
for value_csv2 in value_csv1 :
    csv_value.append(value_csv2)

csvname = csv_value[0]
csvbirthday = csv_value[1]
csvpassword = csv_value[2]


#비밀번호를 각각 한자리 숫자로 변환후 리스트로 반환
passeach = []
pa0 = csv_value[2]
pa1 = list((str(pa0)))
for w in range(2,len(pa1)-2):
    passeach.append(pa1[w])

inputname =
inputbirthday =
inputpassword =




f = open('test.csv', 'w', newline='', encoding="utf-8")
f.write( name+'\n')
f.write(birthday+'\n')
f.write(password)
f.close()





















'''

f = open('test.csv', 'w', newline='', encoding="utf-8")
f.write( name+'\n')
f.write(birthday+'\n')
f.write(password)
f.close()
'''
'''
userpassword = list(map(int,str()))
for i in range(4):
    f.write(str(userpassword[i])+'\n')




#print(fcsv)

for fcsv in csv1 :
    print(fcsv)

#비밀번호를 각각 한자리 숫자로 변환후 리스트로 반환
passeach = []
pa0 = csv1[2]
pa1 = list((str(pa0)))
for w in range(2,len(pa1)-2):
    passeach.append(pa1[w])


for q in passeach:
    print(q)
    
'''