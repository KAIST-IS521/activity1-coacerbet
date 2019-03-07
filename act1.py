import sys
import csv
a1 = sys.argv[1]
a2 = sys.argv[2]
a3 =1
try :
    a2 = int(a2)
except :
    print('please input integer')
    exit(1) #please input integer
if a2<1: 
    print('please input natural number')
    sys.exit(1)#line number should better than 1
with open(a1, newline='') as csvfile:
    snif = csv.Sniffer()
    try :   
        dialect = snif.sniff(csvfile.read(), delimiters=',')
    except :
        print('your csv is not good enough')
        exit(1)
    csvfile.seek(0)
    spamreader = csv.reader(csvfile, dialect, quotechar='"')
    for line in spamreader:
        try :
            line[a2-1]
        except :
            print('please input the number less than the rows')
            sys.exit(1)
    csvfile.seek(0)
    for line in spamreader:
        print(line[a2-1])
