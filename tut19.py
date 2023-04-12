import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['email'])


  # with open ('new_names','csv','w') as new_file:
  #    csv_writer = csv.writer(new_file,delimiter='-')




  ## next(csv_reader)


  # for line in csv_reader:
  #  csv_writer.writerow(line)
  #  print(line[2])