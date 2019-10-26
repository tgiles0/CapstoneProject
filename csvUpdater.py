import csv
import os

if __name__ == '__main__':
    print(os.getcwd())
    # file = os.listdir(os.getcwd() + '\\bots.csv')
    # output_dir = os.getcwd() + '\output'
    # os.mkdir(output_dir)

    with open("bots.csv", "r") as source:
        rdr = csv.reader(source)
        with open("result", "w") as result:
            wtr = csv.writer(result)
            for r in rdr:
                wtr.writerow((r[1], r[2], r[3], r[4],
                              r[7], r[8], r[9], r[10],
                              r[11], r[12], r[13], r[14],
                              r[15], r[17], r[18], r[21],
                              r[22], r[24], r[25], r[26],
                              r[29], r[30], r[31], r[32],
                              r[33], r[34], r[35], r[36],
                              r[40], r[44], r[46], r[48],
                              r[53], r[54], r[55], r[60], r[62]))
