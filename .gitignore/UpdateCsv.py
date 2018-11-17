import pandas as pd

# WinRegistry
#cols = ['source','host']
# TCP FILES
#cols = ['source']
#pollution = r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\csv_files\botsv1.stream_tcp.csv"
#pd.read_csv(pollution, usecols=cols).to_csv(r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\mod_botsv1.stream_tcp.csv", index=False)

#pollution = r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\csv_files\botsv1.winregistry.csv"
#pd.read_csv(pollution, usecols=cols).to_csv(r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\tmp_files\mod_botsv1.winregistry.csv", index=False)

rawCol = ['_raw']

# TCP FILES
# justRaw = r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\csv_files\botsv1.stream_tcp.csv"
# pd.read_csv(justRaw, usecols=rawCol).to_csv(r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\raw_botsv1.stream_tcp.csv", index=False)

#justRaw = r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\csv_files\botsv1.winregistry.csv"
#pd.read_csv(justRaw, usecols=rawCol).to_csv(r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\tmp_files\raw_botsv1.winregistry.csv", index=False)

justRaw = r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\attack_data\stream-tcp-attack-data.csv"
pd.read_csv(justRaw, usecols=rawCol).to_csv(r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\attack_data\raw_stream-tcp-attack-data.csv", index=False)