import pandas as pd
cols = ['_time','date_hour','date_mday','date_month','date_wday','date_year',
        'linecount','timeendpos','timestartpos','type','url']
pollution = r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\bots-v-attack.csv"
pd.read_csv(pollution, usecols=cols).to_csv(r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\condensedAttack.csv", index=False)

rawCol = ['_raw']

justRaw = r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\bots-v-attack.csv"
pd.read_csv(justRaw, usecols=rawCol).to_csv(r"C:\Users\tyler\PycharmProjects\CapstoneProject\dataset\raw_bots-v-attack.csv", index=False)