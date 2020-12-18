import csv
import sys

def writetoCSV(bwFile):
    print("Reading : " + bwFile)
    csv_out_rows = []
    with open(bwFile) as csv_input_file:
        csv_reader = csv.reader(csv_input_file, delimiter=',')
        for row in csv_reader:
            if len(row)>=5 :
                if 'username' != row[1].lower() and 'password' != row[2].lower(): # ignoring header
                    url = row[0]
                    username = row[1]
                    password = row[2]
                    name = row[4]
                    if len(username)>0 and len(password)>0:
                        values = [name, url, username, password]
                        csv_out_rows.append(values)
                else :
                    print("Reading header values")
                
    #print(csv_out_rows)
    outputfile = 'MicrosoftAutofill.csv'
    data_file = open(outputfile, 'w', encoding="utf-8", newline='')
    csv_writer = csv.writer(data_file)
    header = ['name','url','username','password']
    csv_writer.writerow(header)
    csv_writer.writerows(csv_out_rows)
    data_file.close()
    print("Output written : "+ outputfile)


if __name__ == '__main__':
    args_list = sys.argv
    bwFile = args_list[1]
    writetoCSV(bwFile)

