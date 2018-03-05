# import the necessary packages
from PIL import Image
import pytesseract

# 2018 NBA roster, change to state name
nba_teams = {
    # Cities
    "Atlanta",
    "Boston",
    "Brooklyn",
    "Charlotte",
    "Chicago",
    "Cleveland",
    "Dallas",
    "Denver",
    "Detroit",
    "Golden",
    "State",
    "Houston",
    "Indiana",
    "LA",
    "Los",
    "Angeles",
    "Memphis",
    "Miami",
    "Milwaukee",
    "Minnesota",
    "New",
    "Orleans",
    "York",
    "Oklahoma"
    "City",
    "Orlando",
    "Philadelphia",
    "Phoenix",
    "Portland",
    "Sacramento",
    "San",
    "Antonio",
    "Toronto",
    "Utah",
    "Washington",
    # Teams
    "Hawks",
    "Celtics",
    "Nets",
    "Hornets",
    "Bulls",
    "Cavaliers",
    "Mavericks",
    "Nuggets",
    "Pistons",
    "State",
    "Warriors",
    "Rockets",
    "Pacers",
    "Clippers",
    "Lakers",
    "Grizzlies",
    "Heat",
    "Bucks",
    "Timberwolves",
    "Hornets",
    "Knicks",
    "Thunder",
    "Magic",
    "Sixers",
    "Suns",
    "Trail",
    "Blazers",
    "Kings",
    "Spurs",
    "Raptors",
    "Jazz",
    "Wizards"
}


def read_score(frame):
    # TODO: find team names and score from data read
    text = pytesseract.image_to_string(Image.open(frame))
    words = text.split()
    # Catch some misreads also find team names and scores from read data
    
    print(words)
