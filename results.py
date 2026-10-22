import pandas as pd
from pynascar import Race
from races import racesdf

# Format for the results dataframe:
# were using race instead of schedule (going to have results for each race):
# race = Race(seasonyr, 1 (cup series), raceid)


# Exploring what a race result for a single race looks like
race = Race(2025, 1, 5545)
resultsdf = race.results.results
# resultsdf.head()
print(resultsdf.columns.tolist())
# # resultsdf.shape
# # resultsdf.info()
# # resultsdf.describe()
# # resultsdf.isnull().sum()


all_results = []

for races in racesdf['race_id']:
    race = Race(2025, 1, int(races))
    resultsdf = race.results.results
    # Add race_id column
    resultsdf.insert(0, 'race_id', races)
    # These are the columns we are trying to get out of the csv:
    # Race_id, driver_id, driver_name, team_id, team_name, finishing_position
    resultsdf = resultsdf[['race_id', 'driver_id', 'driver_name', 'team', 'team_id', 'starting_position', 'finishing_position']]
    all_results.append(resultsdf)

# print(len(all_results))

resultsdf = pd.concat(all_results, ignore_index=True)

resultsdf.to_csv("results.csv", index=False)


    
