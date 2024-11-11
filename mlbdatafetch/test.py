from functions import players_json, teams_json, gamefeed_json, savant_page_json

# x = players_json(2024)
# player = x[0]
# print(player['id'])
# print(player['i'])

# y = teams_json(1)
# team = y[0]
# print(team['id'])

z = savant_page_json(660271)
print(z['statcast'][0].keys())