import csv
import requests
# Function to create a CSV file from Hacker News item IDs


def create_data_csv_from_ids():
    # Fetch a list of top story IDs from the Hacker News API
    lst_id = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    jsondata = info_lst_from_ids(lst_id)

    # Open a CSV file for writing
    data_file = open('jsondata.csv', 'w', newline='')
    # Convert the retrieved JSON data to CSV
    convert_josn_to_csv(jsondata, data_file )

# Function to retrieve item information from IDs
def info_lst_from_ids(lst_id):
    jsondata = []
    for id in lst_id.json():
        # Fetch individual item information by ID
        response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty')
        if response.status_code == 200:
            jsondata.append(response.json())
    return jsondata

# Function to convert JSON data to CSV
def convert_josn_to_csv(jsondata, data_file):
    csv_writer = csv.writer(data_file)
    count = 0
    for data in jsondata:
        if count == 0:
            # Write the header row using the keys of the first JSON object
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        # Write the data rows using the values of the JSON objects
        csv_writer.writerow(data.values())
    data_file.close()

# Check if the script is being run as the main program
if __name__ == '__main__':
    create_data_csv_from_ids()
