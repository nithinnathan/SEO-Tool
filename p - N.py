from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlrd
import sqlite3

book = xlrd.open_workbook("C:\\Users\\mruser\\Desktop\\N\\book.xlsx")
first_sheet = book.sheet_by_index(0)
cell = first_sheet.cell(0,0)
#print(cell.value)

#url = "http://www.sciencekids.co.nz/sciencefacts/animals/cat.html"
file_handle = urlopen(cell.value)
store = file_handle.read()
f = open("a.txt",'wb')
f.write(store)
f.close()
f1 = open("a.html",'rb')
a = f1.read()
soup = BeautifulSoup(a,"html.parser")
content = soup.get_text()
#print(content)
f2 = open("b.txt",'w')
f2.write(content)
f2.close()

L1 = ["cats","the","kittens"]
s = content.split()
s1 = list(set(s))

#for i in s1:
    #if i in L1:
        #print("Count of",i,"->",s.count(i))

c = sqlite3.connect('nithindb.db')
c.execute('''create table if not exists wordcount1(Word Text not null, Count int not null, Density int not null)''')

count = 0
for i in s1:
    if i in L1:
        count = count + s.count(i)

for i in s1:
    if i in L1:
        e = s.count(i)
        f = (e/count)*100
        c.execute("insert into wordcount1(Word,Count,Density) values(?,?,?)",(i,s.count(i),f))

print("data inserted")

result = c.execute("select * from wordcount1")
for i in result:
    print(i[0],i[1],i[2])
