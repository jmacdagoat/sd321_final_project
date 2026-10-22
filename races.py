from pynascar import Schedule

schedule = Schedule(2025, 1)

# print(schedule.data.head())
print(schedule.data.columns.tolist())


schedule.data.to_csv("nascar_schedule_2025.csv", index=False)

# These are the columns we are trying to get out of the csv:
# raceid, track, date, track type

racesdf = schedule.data[['race_id', 'race_date', 'track_id', 'track_name', 'track_type']]

# print(racesdf.head())
# print(racesdf.info())
# print(racesdf.describe())
print(racesdf.isnull().sum())

racesdf.to_csv("races.csv", index=False)




# five dataframes
# schedule.data
# race.results.results
# race.telemetry.lap_times
# race.telemetry.pit_stops



# explore a dataframe
# df.head()
# df.columns.tolist()
# df.shape
# df.info()
# df.describe()
# df.isnull().sum()