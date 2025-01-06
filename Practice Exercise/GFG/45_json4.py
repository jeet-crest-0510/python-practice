import csv
import json

def make_json(csvFilePath, jsonFilePath):
    
    # create a dictionary
    data = {}
    
    # Open a csv reader called DictReader
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)
        
        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:
            
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['No']
            data[key] = rows
            print(rows)

    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
        
# Driver Code

csvFilePath = 'Practice Exercise\GFG\sample.csv'
jsonFilePath = 'Practice Exercise\GFG\csv_to_json.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)