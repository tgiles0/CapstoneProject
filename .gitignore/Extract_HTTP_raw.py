import os
import re
import csv

# with open('raw_botsv1.winregistry.csv', 'r') as f:
# csv_reader = csv.reader('raw_botsv1.stream_tcp.csv', delimiter=',')

cwd = os.getcwd()
line2 = 0
header = ''
# TCP FILE
# with open('raw_botsv1.stream_tcp.csv', 'r') as f:
# with open('csv_files\\raw_botsv1.stream_smb.csv', 'r') as f:
# with open('tmp_files\\raw_botsv1.stream_ip.csv', 'r') as f:
with open('tmp_files\\raw_botsv1.stream_http.csv', 'r', encoding="utf8") as f:
    lines = f.readlines()
    newLines = []
    headArr = []
    for line in lines:
        if line2 == 0:
            print("On line 1")
            # do nothing
        if line2 >= 1 and len(line) > 3: # line2 % 2 == 1:
            # Most raw files only need these two replacements
            # line = line.replace('"{""', '').replace('}', '')
            # HTTP raw files need more replacements
            line = line.replace('"{""', '').replace('}', '').replace('\r\n', ' ').replace('""\n', '') #.replace('[""', '').replace('""]', '')
            # lineArr = re.split(':|,', line)
            lineArr = re.split('"":""|"",""|"":|,""', line)
            # get rid of cs_version data from last to first.
            #del (lineArr[30])
            #del (lineArr[29])
            #del (lineArr[28])
            """if line2 > 500000 + 1:
                print("At failing point")"""
            #print('Processing line')
            newLine = ''
            i = 0
            while i < len(lineArr):
                # get rid of unused endtime data
                if 'endtime' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused endtime data
                if 'accept' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused accept_language data
                if 'accept_language' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused cookie data
                if 'cookie' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused cs_content_length data
                if 'cs_content_length' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused cs_content_type data
                if 'cs_content_type' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused cs_date data
                if 'cs_date' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused cs_cache_control data
                if 'cs_cache_control' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused cs_pragma data
                if 'cs_pragma' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused cs_version data
                if 'cs_version' in lineArr[i]:
                    while 'data_center_time' not in lineArr[i]:
                        del (lineArr[i])
                # get rid of unused dest_content data
                if 'dest_content' in lineArr[i]:
                    while 'dest_headers' not in lineArr[i]:
                        del (lineArr[i])
                # get rid of unused dest_headers data
                if 'dest_headers' in lineArr[i]:
                    while 'dest_ip' not in lineArr[i]:
                        del (lineArr[i])
                # get rid of unused src_content data
                if 'src_content' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused etag data
                if 'etag' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused location data
                if 'location' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused expires data
                if 'expires' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused http_referrer data
                if 'http_referrer' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused set_cookie data
                if 'set_cookie' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # get rid of unused sc_pragma data
                if 'sc_pragma' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                if 'transfer_encoding' in lineArr[i]:
                    # delete the identifier and the value
                    del (lineArr[i])
                    del (lineArr[i])
                # Extract logic for HTTP
                # not all lines have same values in them. Some missing the uri_query
                if i > 1 and i < len(lineArr):
                    if i % 2 == 0 and line2 == 1:
                        if i != len(lineArr) - 2:
                            header += lineArr[i] + ','
                        else:
                            header += lineArr[i]
                        headArr.append(lineArr[i])
                    # if the identifier was mapped in the header and we can go forward in the lineArr then do it.
                    #if len(headArr) != 57:
                    #    headArr = re.split(',', header)
                    headerI = int(i/2) - 1
                    if lineArr[i] == headArr[headerI]: # and i + 1 < 112:
                        i += 1
                        # replace any commas found
                        if ',' in lineArr[i]:
                            lineArr[i] = lineArr[i].replace(',', '{COMMA}')
                        if '"' in lineArr[i]:
                            lineArr[i] = lineArr[i].replace('"', '')
                        if i != len(lineArr) - 1:
                            newLine += lineArr[i] + ','
                        else:
                            newLine += lineArr[i]
                    # Missing value
                    # May need to check each line if we have mapped a value for each column or just a ','
                    else:
                        ok = True
                        while (lineArr[i] != headArr[headerI]) and ok:
                            newLine += ','
                            # Index i should be the label value not found in header.
                            # increment by 2 to get to the next value of the header.
                            # don't increment i as elements were missing from the line.
                            j = i + 2
                            headerI = int(j/2) - 1
                            # break out of loop if index is to high.
                            if headerI >= len(headArr):
                                ok = False
                    # 111 should be the value of uri_path, which comes right before uri_query
                    #if (i == 111) and ('uri_query' not in lineArr):
                    #    newLine += ','
                # extract logic for smb
                """if i > 1 and i < 26:
                    if i % 2 == 0 and line2 == 1:
                        if i != 24:
                            header += lineArr[i] + ','
                        else:
                            header += lineArr[i]
                    elif i % 2 != 0:
                        if '"' in lineArr[i]:
                            lineArr[i] = lineArr[i].replace('"', '')
                        if i != 25:
                            newLine += lineArr[i] + ','
                        else:
                            newLine += lineArr[i]"""
                # extract logic for IP
                """ if i > 1 and i < 32:
                    if i % 2 == 0 and line2 == 1:
                        if i != 30:
                            header += lineArr[i] + ','
                        else:
                            header += lineArr[i]
                    elif i % 2 != 0:
                        if i != 31:
                            newLine += lineArr[i] + ','
                        else:
                            newLine += lineArr[i]"""
                # extract logic for TCP
                """if i > 1 and i < 60:
                    if i % 2 == 0 and line2 == 1:
                        if i != 58:
                            header += lineArr[i] + ','
                        else:
                            header += lineArr[i]
                    elif i % 2 != 0:
                        if i != 59:
                            newLine += lineArr[i] + ','
                        else:
                            newLine += lineArr[i]"""
                i += 1
            if line2 == 1:
                header += '\n'
                newLines.append(header)
            newLine += '\n'
            newLines.append(newLine)
        line2 += 1


    newFile = 'tmp_files\\NewRaw_botsv1.stream_http.csv'
    with open(newFile, 'w') as w:
        w.writelines(newLines)

