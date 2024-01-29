import csv

l = ["aaaa", "ssss", "ssss"]



with open('one.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file,)
    for i in l:
        csv_writer.writerows(i)
