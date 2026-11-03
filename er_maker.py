import os
import pandas as pd
## looked up OS syntax to cd back to bigger file
os.chdir('..')



## from events table create race_events and flag info
events_df = pd.read_csv("events.csv")
events_df.index=range(1,len(events_df)+1)
events_df.index = 'e' + events_df.index.astype(str)
events_df.index.name='event_ID'

events_df=events_df.reset_index()
#print(events_df)



##from events create flag dataset
flag_df= events_df[['Flag_State', 'Flag']]


##race_events from events
race_events_df =  events_df[['event_ID', 'race_id']]

## Race from races.csv
races_df= pd.read_csv('races.csv')
tracks_raw_df = races_df
races_df = races_df[['race_id', 'race_date', 'track_id']]

## Track from Rraces_df
track_df = tracks_raw_df[['track_id', 'track_name', 'track_type']]

## Track_Info from Track
track_info_df = tracks_raw_df[['track_type']].drop_duplicates()
track_info_df.index=range(1,len(track_info_df)+1)
track_info_df.index.name='track_Type_ID'
track_info_df=track_info_df.reset_index()

## Team_Info and Driver_Info from results.csv
results_df = pd.read_csv('results.csv')
team_df = results_df[['team_id', 'team']]
driver_df = results_df[['driver_id', 'driver_name', 'team_id']]
final_results_df = results_df[['race_id', 'driver_id', 'starting_position', 'finishing_position']]

## Lap_Info from laptimes.csv
laptimes_df = pd.read_csv('laptimes.csv')
lap_info_df = laptimes_df[['driver_id', 'race_id', 'Lap', 'position', 'lap_speed']]

## Pitstop_Info from pitstops.csv
pitstops_df = pd.read_csv('pitstops.csv')
pitstop_info_df = pitstops_df[['race_id', 'driver_id', 'lap', 'total_duration', 'positions_gained_lost']]


##create csvs for everything
os.chdir('er_relations')
events_df.to_csv("Events.csv", index=False)
flag_df.to_csv("Flag_info.csv", index=False)
race_events_df.to_csv("Race_Events.csv", index=False)
races_df.to_csv("Race.csv", index=False)
track_df.to_csv("Track.csv", index=False)
track_info_df.to_csv("Track_Info.csv", index=False)
team_df.to_csv("Team_Info.csv", index=False)
driver_df.to_csv("Driver_Info.csv", index=False)
final_results_df.to_csv("Results.csv", index=False)
lap_info_df.to_csv("Lap_Info.csv", index=False)
pitstop_info_df.to_csv("Pitstop_Info.csv", index=False)