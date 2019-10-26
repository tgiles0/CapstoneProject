"""_raw
"08/24/2016 12:27:42.110
event_status=""(0)The operation completed successfully.""
pid=708
process_image=""c:\Windows\System32\svchost.exe""
registry_type=""CreateKey""
key_path=""HKLM\system\controlset001\control\deviceclasses""
data_type=""REG_NONE""
data="""

lineCount = 0
#             0    ,      1     , 2 ,       3     ,       4     ,  5     ,   6     , 7
header = 'timestamp,event_status,pid,process_image,registry_type,key_path,data_type,data\n'
newLines = []
newLines.append(header)
newLine = ''

with open('tmp_files\\raw_botsv1.winregistry.csv', 'r') as f:
    lines = f.readlines()
    i = 0
    updateLine = ''
    # handle when data= field spans 2 lines.
    while i < len(lines):
        if 'data=' in lines[i]:
            # check if next line has 3 """ in it i.e. data= spans to next line
            if i + 1 < len(lines) and '"""' in lines[i+1]:
                # get rid of new line on first line of data=
                lines[i] = lines[i].rstrip()
                # set updateLine to [1st data= line] + ' ' + [2nd data= line]
                updateLine = lines[i] + ' ' + lines[i+1]
                # redefine lines[i]
                lines[i] = updateLine
                # delete the 2nd data= line
                del lines[i+1]
                print('found multi-line data=')
                print(len(lines))
                # reset updateLine
                updateLine = ''
        i += 1
    for line in lines:
        if lineCount == 0:
            print("On line 1")
            # do nothing
        if lineCount >= 1:
            line = line.replace('"', '').rstrip()
            if lineCount % 8 == 1:
                newLine += line + ','
            if lineCount % 8 == 2:
                line = line.replace('event_status=', '')
                newLine += line + ','
            if lineCount % 8 == 3:
                line = line.replace('pid=', '')
                newLine += line + ','
            if lineCount % 8 == 4:
                line = line.replace('process_image=', '')
                newLine += line + ','
            if lineCount % 8 == 5:
                line = line.replace('registry_type=', '')
                newLine += line + ','
            if lineCount % 8 == 6:
                # sometimes key_path= contains commas which we cannot have. Replace them!
                line = line.replace('key_path=', '').replace(',', '{COMMA}')
                newLine += line + ','
            if lineCount % 8 == 7:
                line = line.replace('data_type=', '')
                newLine += line + ','
            if lineCount % 8 == 0:
                # sometimes data= contains commas which we cannot have. Replace them!
                line = line.replace('data=', '').replace(',', '{COMMA}')
                # Add '\n' since this is the last column
                newLine += line + '\n'
                # newLine row is now full add it to newLines
                newLines.append(newLine)
                # reset the newLine for next row
                newLine = ''
        # increment our line counter
        lineCount += 1
    newFile = 'tmp_files\\NewRaw_botsv1.winregistry.csv'
    with open(newFile, 'w') as w:
        w.writelines(newLines)
