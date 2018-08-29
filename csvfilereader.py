import csv

with open('report.csv') as csvfile:
    csvfileread = csv.reader(csvfile, delimiter=',')
    service = []
    operation = []
    usagetype = []
    resouce = []
    starttime = []
    endtime = []
    usage = []
    for row in csvfileread:
        opr = row[0]
        usgt = row[1]
        startt = row[2]
        endt = row[3]
        usg = row[4]
        operation.append(opr)
        usagetype.append(usgt)
        starttime.append(startt)
        endtime.append(endt)
        usage.append(usg)
 
unique_ops = set(operation)
# print(usage)
ops_dict = dict()
with open ('report.csv') as csvfile:
    csvfileread = csv.reader(csvfile, delimiter=',')
    for row in csvfileread:
        opr = row[0]
        usg = row[4]
        if opr not in ops_dict:
            ops_dict[opr] = usg
        else:
            ops_dict[opr] = float(float(ops_dict[opr]) +float(usg))
for item in sorted(ops_dict.items()):
    print(item)

