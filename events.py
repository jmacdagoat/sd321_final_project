import pandas as pd
from pynascar import Race
from races import racesdf

# Explore what a single race looks like

# race = Race(2025, 1, 5546, reload=True)
# eventsdf = race.telemetry.events

# # # Explore the dataframe
# # # print(pitdf.head())
# # # print(pitdf.info())
# # # print(pitdf.describe())
# # print(eventsdf.isnull().sum())
# # print(eventsdf.columns.tolist())

all_events = []

for races in racesdf['race_id']:
    race = Race(2025, 1, int(races))
    eventsdf = race.telemetry.events
    if eventsdf.empty:
        continue
    # Add race_id column
    eventsdf.insert(0, 'race_id', races)
    # These are the columns we are trying to get out of the csv:
    # Race_id, driver_id, pit_stop_duration, positions_gained_lost
    eventsdf = eventsdf[['race_id', 'Lap', 'Flag_State', 'Flag', 'note']]
    all_events.append(eventsdf)

eventsdf = pd.concat(all_events, ignore_index=True)
# print(len(all_events))
eventsdf.to_csv("events.csv", index=False)