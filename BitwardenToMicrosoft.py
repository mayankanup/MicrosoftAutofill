import json 
import csv
import sys

def writetoCSV(bwFile):
    print("Reading : " + bwFile)
    csv_rows = []
    with open(bwFile, encoding='utf-8') as json_file: 
        data = json.load(json_file)
        items = data['items']
        for item in items:
            login = item.get('login')
            name = item.get('name')
            if login:
                username = login['username']
                password = login['password']
                uris = login['uris']
                for uri in uris:
                    urival = uri["uri"]
                    values = [name, urival, username, password]
                    csv_rows.append(values)
            else:
                print("Login not found in "+name)
    #print(csv_rows)
    outputfile = 'MicrosoftAutofill.csv'
    data_file = open(outputfile, 'w', encoding="utf-8", newline='')
    csv_writer = csv.writer(data_file)
    header = ['name','url','username','password']
    csv_writer.writerow(header)
    csv_writer.writerows(csv_rows)
    data_file.close()
    print("Output written : "+ outputfile)


if __name__ == '__main__':
    args_list = sys.argv
    bwFile = args_list[1]
    writetoCSV(bwFile)

