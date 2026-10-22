import pandas as pd
from pynascar import Race
from races import racesdf

# Looking at what laptimes for one race looks like
# race = Race(2025, 1, 5550, reload=True)
# laptimesdf = race.telemetry.lap_times
# print(laptimesdf.columns.tolist())
# explore the dataframe
# laptimesdf.head()
# laptimesdf.columns.tolist()
# laptimesdf.shape
# laptimesdf.info()
# laptimesdf.describe()
# laptimesdf.isnull().sum()



all_laps = []

for races in racesdf["race_id"]:
    race = Race(2025, 1, races, reload=True)
    # Some races don't have lap data, just don't include
    lapsdf = race.telemetry.lap_times
    if lapsdf.empty:
        continue
    lapsdf.insert(0, 'race_id', races)
    # These are the columns we are trying to get out of the csv:
    # race_id, driver_name, driver_id, Lap, lap_speed, position (not including lap_tiime because we noticed some issues in the units and precision)
    lapsdf = lapsdf[['race_id', 'driver_name', 'driver_id', 'Lap', 'lap_speed', 'position']]
    lapsdf['driver_id'] = lapsdf['driver_id'].astype('Int64') # Use Int64 incase some values are missing
    all_laps.append(lapsdf)

# print(len(all_laps))

lapsdf = pd.concat(all_laps, ignore_index=True)
lapsdf.to_csv("laptimes.csv", index=False)


