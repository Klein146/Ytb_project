import csv
import json

with open('JSON_f.json') as JSON_PATH:
    data = json.load(JSON_PATH)

# now we will open a file for writing
data_file = open('DATA_f.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file

result = []
for items in data['items']:

        # Writing headers of CSV file
    authors = items['snippet']['topLevelComment']['snippet']['authorDisplayName']
    comment = items['snippet']['topLevelComment']['snippet']['textOriginal']
    result.append([authors, comment])
        # csv_writer.writerow()

    # Writing data of CSV file
csv_writer.writerows(result)

data_file.close()
