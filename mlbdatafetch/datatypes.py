from dataclasses import dataclass
from typing import List, TypeVar, Generic
from datetime import date
import pandas as pd

GenericEntry = TypeVar('GenericEntry', bound='Entry')

@dataclass
class Entry:
    def to_series(self) -> pd.Series:
        return pd.Series(self.__dict__)

class EntryList(List[GenericEntry], Generic[GenericEntry]):
    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame([e.__dict__ for e in self])

@dataclass
class Player(Entry):
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

@dataclass
class Team(Entry):
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

@dataclass
class Venue(Entry):
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

@dataclass
class Game(Entry):
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

@dataclass
class DefensePlay(Entry):
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

@dataclass
class Pitch(Entry):
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

@dataclass
class BatterBoxscore(Entry):
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

@dataclass
class PitcherBoxscore(Entry):
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

@dataclass
class GamefeedResponse:
    game: Game
    pitches: EntryList[Pitch]
    batter_boxscores: EntryList[BatterBoxscore]
    pitcher_boxscores: EntryList[PitcherBoxscore]