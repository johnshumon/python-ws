import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csv_file_path, json_file_path):
    # create list
    data_list = []

    # open a csv dictionary reader
    with open(csv_file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # convert each row into a list object
        # and append to the list
        for row in csv_reader:
            data_list.append(row)

    # open a json writer and dump data_list to the file
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data_list, indent=4))


# Decide the two file paths according to your
# computer system
csvFilePath = r'Backend_cases.csv'
jsonFilePath = r'Backend_cases_list.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
