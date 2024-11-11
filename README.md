# mlb-data-fetch
Get Dataframes and JSON about MLB teams, players, games, plays, and Statcast data

## Example Usage
```python
from mlb_data_fetch import mlb_data_fetch

# Get all teams as a DataFrame
teams_df = mlb_data_fetch.get_teams()

# Get all teams as JSON
teams_json = mlb_data_fetch.get_teams(as_json=True)
```
-show pic of teams_df here-
