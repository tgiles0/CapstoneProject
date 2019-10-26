import re
import csv

line2 = 0

with open('attack_data\\NewRaw_stream-tcp-attack-data.csv', 'r') as f:
    attackTcpTimestamps = f.readlines()

with open('complete_data\\p-attack-data.csv', 'r') as f:
    unclassifiedTimes = f.readlines()


# keep track of all indexes 