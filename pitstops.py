import pandas as pd
from pynascar import Race
from races import racesdf

# Explore what a single race looks like

# race = Race(2025, 1, 5546, reload=True)
# pitdf = race.telemetry.pit_stops

# Explore the dataframe
# print(pitdf.head())
# print(pitdf.info())
# print(pitdf.describe())
# print(pitdf.isnull().sum())
# print(pitdf.columns.tolist())

all_pits = []

for races in racesdf['race_id']:
    race = Race(2025, 1, int(races))
    pitsdf = race.telemetry.pit_stops
    if pitsdf.empty:
        continue
    # Add race_id column
    pitsdf.insert(0, 'race_id', races)
    # These are the columns we are trying to get out of the csv:
    # Race_id, driver_id, pit_stop_duration, positions_gained_lost
    pitsdf = pitsdf[['race_id', 'driver_id', 'lap', 'total_duration', 'positions_gained_lost']]
    pitsdf['driver_id'] = pitsdf['driver_id'].astype('Int64')
    all_pits.append(pitsdf)

pitsdf = pd.concat(all_pits, ignore_index=True)
# print(len(all_pits))
pitsdf.to_csv("pitstops.csv", index=False)