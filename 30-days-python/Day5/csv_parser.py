# import csv and Path modules
import csv
from pathlib import Path


#create the file path of the sample_file

file_path = Path(__file__).parent/"players.csv"
master_list = []
#print(path_file)

with open(file_path, "r") as file:
    reader = csv.reader(file) #
    header = next(reader) # ['Name', 'Team', 'Role', 'Runs', ...]

    name_idx = header.index("Name")
    team_idx = header.index("Team")
    runs_idx = header.index("Runs")

    for row in reader:
        player_data = [row[name_idx], row[team_idx], row[runs_idx]]
        master_list.append(player_data)

print(master_list)