# MLB Data Tools
DataFrames, type-safety, and plotting for modern baseball analytics.

## Philosophy & Goals
- Expose useful endpoints and datasets (Savant Player Pages, OAA data by play, pitch by pitch statcast)
- Defined data schema/types
- Easily convert to DataFrames

## Installation
```
pip install mlbdatatools
```

## Example Usage
```python
from mlbdatatools import mlbfetch

# fetch opening day games for the 2024 season
opening_day_games = mlbfetch.schedule("2024-03-28")

# print the home and away team names for the first game
print(
    opening_day_games[0].home_team_name,
    opening_day_games[0].away_team_name
)

# convert the games to a pandas DataFrame for analysis
games_df = opening_day_games.to_df()
print(games_df.head())
```

```
Baltimore Orioles Los Angeles Angels
```

|   | id     | type | doubleheader | season | game_date   | game_time  | status_code | home_team_id | away_team_id | home_team_name       | away_team_name        | venue_id | venue_name                     | weather_condition | weather_temp | weather_wind         | home_team_pitcher_id | home_team_pitcher_name | away_team_pitcher_id | away_team_pitcher_name |
|---|--------|------|--------------|--------|-------------|------------|-------------|--------------|--------------|-----------------------|-----------------------|----------|--------------------------------|--------------------|--------------|----------------------|----------------------|------------------------|----------------------|------------------------|
| 0 | 747060 | R    | N            | 2024   | 2024-03-28  | 19:05:00Z | F           | 110          | 108          | Baltimore Orioles     | Los Angeles Angels    | 2        | Oriole Park at Camden Yards    | Cloudy             | 54           | 9 mph, In From LF    | 669203               | Corbin Burnes          | 663776               | Patrick Sandoval       |


## Plotting
```python
from mlbdatatools import mlbfetch, mlbplot

pitches_df = mlbfetch.gamefeed(747846).pitches.to_df()


```