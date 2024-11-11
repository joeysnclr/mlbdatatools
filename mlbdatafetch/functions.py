import requests
import json
import ast
from datetime import date
from typing import TypedDict

class Player(TypedDict):
    id: int
    full_name: str
    first_name: str
    last_name: str
    primary_number: str
    birth_country: str
    height: str
    weight: str
    active: str
    current_team_id: int
    primary_position_code: str
    primary_position_abbrev: str
    draft_year: int
    bat_side: str
    pitch_hand: str
    strike_zone_top: float
    strike_zone_bottom: float

class Team(TypedDict):
    id: int
    name: str
    season: int
    venue_id: int
    venue_name: str
    team_code: str
    abbreviation: str
    team_name: str
    location_name: str
    league_id: int
    league_name: str
    division_id: int
    division_name: str
    sport_id: int
    sport_name: str
    parent_org_id: int | None
    parent_org_name: str | None

class Venue(TypedDict):
    id: int
    name: str
    turf_type: str | None
    roof_type: str | None
    left_line: int | None
    left: int | None
    left_center: int | None
    center: int | None
    right_center: int | None
    right: int | None
    right_line: int | None
    azimuth_ange: int | None
    elevation: int | None

class Game(TypedDict):
    id: int
    type: str
    doubleheader: str
    season: str
    game_date: date
    game_time: str
    status_code: str
    home_team_id: int
    away_team_id: int
    home_team_name: str
    away_team_name: str
    venue_id: int
    venue_name: str
    weather_condition: str
    weather_temp: str
    weather_wind: str
    home_team_pitcher_id: int
    home_team_pitcher_name: str
    away_team_pitcher_id: int
    away_team_pitcher_name: str

class Pitch(TypedDict):
    id: int
    inning: int
    ab_number: int
    batter: int
    stand: str
    pitcher: int
    p_throws: str
    team_batting_id: int
    team_fielding_id: int
    result: str
    events: str
    strikes: int
    balls: int
    outs: int
    pitch_type: str
    call: str
    pitch_call: str
    is_strike_swinging: bool
    start_speed: float | None
    extension: float | None
    zone: int | None
    spin_rate: float | None
    x0: float | None
    z0: float | None
    breakx: float | None
    breakz: float | None
    inducedbreakz: float | None
    hit_speed: float | None
    xba: float | None
    hit_angle: float | None
    is_barrel: bool | None
    pitch_number: int
    gameid: int
    px: float | None
    pz: float | None
    y0: float | None
    ax: float | None
    ay: float | None
    az: float | None
    vx0: float | None
    vy0: float | None
    vz0: float | None
    hc_x_ft: float | None
    hc_y_ft: float | None
    runner_on_1b: bool
    runner_on_2b: bool
    runner_on_3b: bool
    runner_batter_score: bool
    runner_1b_score: bool
    runner_2b_score: bool
    runner_3b_score: bool

class BatterBoxscore(TypedDict):
    id: str
    playerid: int
    gameid: int
    flyouts: int
    groundouts: int
    runs: int
    homeruns: int
    strikeouts: int
    baseonballs: int
    hits: int
    atbats: int
    caughtstealing: int
    stolenbases: int
    plateappearances: int
    rbi: int
    doubles: int
    triples: int
    hitbypitch: int

class PitcherBoxscore(TypedDict):
    id: str
    playerid: int
    gameid: int
    groundouts: int
    airouts: int
    runs: int
    strikeouts: int
    baseonballs: int
    hits: int
    hitbypitch: int
    atbats: int
    numberofpitches: int
    inningspitched: float
    wins: int
    losses: int
    earnedruns: int
    battersfaced: int
    outs: int
    balls: int
    strikes: int

class GamefeedResponse(TypedDict):
    game: Game
    pitches: list[Pitch]
    batter_boxscores: list[BatterBoxscore]
    pitcher_boxscores: list[PitcherBoxscore]

class DefensePlay(TypedDict):
    fielder_id: str
    fielder_name: str
    fielder_team_id: str
    fielder_position: int
    year: str
    month: str
    est_success: float
    outs_above_avg: float
    runs_prevented: float
    is_out: bool

def get_request_json(url: str):
    r = requests.get(url)
    return r.json()

def get_request_html(url:str) -> str:
    r = requests.get(url)
    return r.text

def extract_js_var_from_html(html: str, var_name: str, extract_keys: list[str]):
    var_text = html.split(f"var {var_name} = ")[1].split(";")[0]
    result_dict = {}
    for line in var_text.split("\n"):
        for key in extract_keys:
            if f"{key}: " in line:
                value = line.split(f"{key}: ")[1][:-1]
                result_dict[key] = json.loads(value)
    return result_dict

def players_json(season: int) -> list[Player]:
    players_url = "https://statsapi.mlb.com/api/v1/sports/1/players"
    players_raw = get_request_json(players_url).get('people')
    players_clean = [Player(
        id=p.get('id'),
        full_name=p.get('fullName'),
        first_name=p.get('firstName'),
        last_name=p.get('lastName'),
        primary_number=p.get('primaryNumber'),
        birth_country=p.get('birthCountry'),
        height=p.get('height'),
        weight=p.get('weight'),
        active=p.get('active'),
        current_team_id=p.get('currentTeam').get('id'),
        primary_position_code=p.get('primaryPosition').get('code'),
        primary_position_abbrev=p.get('primaryPosition').get('abbreviation'),
        draft_year=p.get('draftYear'),
        bat_side=p.get('batSide').get('code'),
        pitch_hand=p.get('pitchHand').get('code'),
        strike_zone_top=p.get('strikeZoneTop'),
        strike_zone_bottom=p.get('strikeZoneBottom')
    ) for p in players_raw]
    return players_clean

def teams_json(league_id: int) -> list[Team]:
    teams_url = "https://statsapi.mlb.com/api/v1/teams"
    teams_raw = get_request_json(teams_url).get('teams')
    teams_clean = [Team(
        id=t.get('id'),
        name=t.get('name'),
        season=t.get('season'),
        venue_id=t.get('venue').get('id'),
        venue_name=t.get('venue').get('name'),
        team_code=t.get('teamCode'),
        abbreviation=t.get('abbreviation'),
        team_name=t.get('teamName'),
        location_name=t.get('locationName'),
        league_id=t.get('league').get('id'),
        league_name=t.get('league').get('name'),
        division_id=t.get('division').get('id'),
        division_name=t.get('division').get('name'),
        sport_id=t.get('sport').get('id'),
        sport_name=t.get('sport').get('name'),
        parent_org_id=t.get('parentOrgId'),
        parent_org_name=t.get('parentOrgName')
    ) for t in teams_raw]
    return teams_clean

def venues_json(league_id: int) -> list[Venue]:
    venues_url = "https://ws.statsapi.mlb.com/api/v1/venues?hydrate=fieldInfo,location"
    venues_raw = get_request_json(venues_url)
    venues_clean = [
        Venue(
            id=v.get('id'),
            name=v.get('name'),
            turf_type=v.get('fieldInfo', {}).get('turfType'),
            roof_type=v.get('fieldInfo', {}).get('roofType'),
            left_line=v.get('fieldInfo', {}).get('leftLine'),
            left=v.get('fieldInfo', {}).get('left'),
            left_center=v.get('fieldInfo', {}).get('leftCenter'),
            center=v.get('fieldInfo', {}).get('center'),
            right_center=v.get('fieldInfo', {}).get('right_center'),
            right=v.get('fieldInfo', {}).get('right'),
            right_line=v.get('fieldInfo', {}).get('right_line'),
            azimuth_ange=v.get('location', {}).get('azimuthAngle'),
            elevation=v.get('location', {}).get('elevation'),
        ) for v in venues_raw
    ]
    return venues_clean

def gamefeed_json(game_id: int) -> dict:
    gamefeed_url = f"https://ws.statsapi.mlb.com/api/v1.1/game/{game_id}/feed/live"
    return get_request_json(gamefeed_url)

def defense_plays_json(entity_id: int) -> list[DefensePlay]:
    plays_url = f"https://baseballsavant.mlb.com/visuals/oaa-data?type=Fielder&playerId={entity_id}&startYear=2024&endYear=2024"
    plays_raw = get_request_json(plays_url)
    plays_clean = [
        DefensePlay(
            fielder_id=p.get("target_mlb_id"),
            fielder_name=p.get("name_fielder"),
            fielder_team_id=p.get("fld_team_id"),
            fielder_position=p.get("target_id"),
            year=p.get("year"),
            month=p.get("api_game_date_month_mm"),
            est_success=p.get("adj_estimated_success_rate"),
            outs_above_avg=p.get("outs_above_average"),
            runs_prevented=p.get("fielding_runs_prevented"),
            is_out=p.get("is_hit_into_play_field_out")=="1"
        ) for p in plays_raw
    ]
    return plays_clean

def savant_page_json(player_id: int, batter=True) -> dict:
    player_type_param = "statcast-r-pitching-mlb" if not batter else "statcast-r-batting-mlb"
    player_page_url = f"https://baseballsavant.mlb.com/savant-player/shohei-ohtani-{player_id}?stats={player_type_param}"
    page_html = get_request_html(player_page_url)
    dict_from_js = extract_js_var_from_html(page_html, "serverVals", ['statcast', 'metricSummaryStats', 'rangeLine', 'zones', 'movement', 'pitchDistribution', 'pitchTypeSamples', 'leaguePitchMovement', 'pitcherArmAngles', 'pitchTypes', 'statcastGameLogs'])
    return dict_from_js




