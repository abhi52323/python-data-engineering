# write list Comprehension to find all players with more than 5000 runs.

#import csv and path modules

import csv
from pathlib import Path

file_path = Path(__file__).parent/"players.csv"
master_list = []
required_keys = ["Name","Team","Runs"]

with open(file_path,"r") as file:
    reader = csv.DictReader(file)

    for rows in reader:
        if int(rows["Runs"]) > 5000:
            players_data = {key: rows[key] for key in required_keys}
            master_list.append(players_data)

print(master_list)
