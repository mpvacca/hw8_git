import csv

S1avg, S1Min, S1Max = 0.0, 50, 0
S2avg, S2Min, S2Max = 0.0, 50, 0
S3avg, S3Min, S3Max = 0.0, 50, 0
S4avg, S4Min, S4Max = 0.0, 50, 0
S5avg, S5Min, S5Max = 0.0, 50, 0
    
with open('raw_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print('\t\t\t\tSummary of Raw Data from Sensors')
            line_count += 1
        elif line_count == 1:
            print('\t\t   Average\t\tMinimum Reading\t\tMaximum Reading')
            line_count += 1
        else:
            S1avg = S1avg + float(row[0])
            if int(row[0]) < S1Min:
                S1Min = int(row[0])
            if int(row[0]) > S1Max:
                S1Max = int(row[0])
            S2avg = S2avg + float(row[1])
            if int(row[1]) < S2Min:
                S2Min = int(row[1])
            if int(row[1]) > S2Max:
                S2Max = int(row[1])
            S3avg = S3avg + float(row[2])
            if int(row[2]) < S3Min:
                S3Min = int(row[2])
            if int(row[2]) > S3Max:
                S3Max = int(row[2])
            S4avg = S4avg + float(row[3])
            if int(row[3]) < S4Min:
                S4Min = int(row[3])
            if int(row[3]) > S4Max:
                S4Max = int(row[3])
            S5avg = S5avg + float(row[4])
            if int(row[4]) < S5Min:
                S5Min = int(row[4])
            if int(row[4]) > S5Max:
                S5Max = int(row[4])
            line_count += 1
    S1avg = round(S1avg/6000,3)
    S2avg = round(S2avg/6000,3)
    S3avg = round(S3avg/6000,3)
    S4avg = round(S4avg/6000,3)
    S5avg = round(S5avg/6000,3)
    print 'Sensor 1\t', S1avg, '\t\t\t  ', S1Min, '\t\t\t\t  ', S1Max
    print 'Sensor 2\t', S2avg, '\t\t\t  ', S2Min, '\t\t\t\t  ', S2Max
    print 'Sensor 3\t', S3avg, '\t\t\t  ', S3Min, '\t\t\t\t  ', S3Max
    print 'Sensor 4\t', S4avg, '\t\t\t  ', S4Min, '\t\t\t\t  ', S4Max
    print 'Sensor 5\t', S5avg, '\t\t\t  ', S5Min, '\t\t\t\t  ', S5Max
