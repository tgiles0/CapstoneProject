import os
import re
import csv

# with open('raw_botsv1.winregistry.csv', 'r') as f:
# csv_reader = csv.reader('raw_botsv1.stream_tcp.csv', delimiter=',')

cwd = os.getcwd()
line2 = 0

# TCP FILE
with open('raw_botsv1.stream_tcp.csv', 'r') as f:
    lines = f.readlines()
    newLines = []
    for line in lines:
        if line2 == 0:
            print("On line 1")
            # do nothing
        if line2 >= 1 and line2 % 2 == 1:
            # print("On line 2")
            line = line.replace('"{""', '').replace('}', '')
            lineArr = re.split('"":""|"",""|"":|,""', line)
            #print('Processing line')
            header = ''
            newLine = ''
            i = 0
            while i < len(lineArr):
                if i > 1 and i < 60:
                    if i % 2 == 0 and line2 == 1:
                        if i != 58:
                            header += lineArr[i] + ','
                        else:
                            header += lineArr[i]
                    elif i % 2 != 0:
                        if i != 59:
                            newLine += lineArr[i] + ','
                        else:
                            newLine += lineArr[i]
                i += 1
            if line2 == 1:
                header += '\n'
                newLines.append(header)
            newLine += '\n'
            newLines.append(newLine)
        line2 += 1


    newFile = 'tmp_files\\NewRaw_botsv1.stream_tcp.csv'
    with open(newFile, 'w') as w:
        w.writelines(newLines)

#csv_reader0 = csv.reader(, delimiter=',')
#for row in csv_reader0:
#    row.split()

