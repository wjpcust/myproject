import csv

file1 = open("E:/EdgeDownload/archive/GBvideos.csv","r",encoding="UTF-8")
file2 = open("E:/EdgeDownload/archive/USvideos.csv","r",encoding="UTF-8")

fileReader1 = list(csv.reader(file1))
fileReader2 = list(csv.reader(file2))
del fileReader1[0]
del fileReader2[0]

file_1 = open('E:/GB_video_data.csv','w',encoding='UTF-8')
file_2 = open('E:/US_video_data.csv','w',encoding='UTF-8')
for i in fileReader1:
    file_1.write(f'{i[7]},')
    file_1.write(f'{i[8]},')
    file_1.write(f'{i[9]},')
    file_1.write(f'{i[10]}\n')
for j in fileReader2:
    file_2.write(f'{j[7]},')
    file_2.write(f'{j[8]},')
    file_2.write(f'{j[9]},')
    file_2.write(f'{j[10]}\n')
file1.close()
file2.close()
file_1.close()
file_2.close()