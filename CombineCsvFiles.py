import pandas as pd

pieces = []

# TCP Files
s = pd.read_csv(r'C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\mod_botsv1.stream_tcp.csv') # your directory
# s = pd.read_csv(r'C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\tmp_files\mod_botsv1.winregistry.csv')
pieces.append(s)
# s = pd.read_csv(r'C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\tmp_files\NewRaw_botsv1.winregistry.csv')
s = pd.read_csv(r'C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\tmp_files\NewRaw_botsv1.stream_tcp.csv')
pieces.append(s)

newcsv = pd.concat(pieces, axis=1) # this will yield multiple columns
# TCP Files
newcsv.to_csv(r'Updated_botsv1.stream_tcp.csv')
# WinRegistry File
# newcsv.to_csv(r'Updated_botsv1.winregistry.csv')