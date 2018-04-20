# import the necessary packages
from PIL import Image
from ErrorCorrection import common_misreads
from GameStatus import GameStatus
import pytesseract

# 2018 NBA roster, change to state name
nba_teams = {
    # Cities
    "atlanta",
    "boston",
    "brooklyn",
    "charlotte",
    "chicago",
    "cleveland",
    "dallas",
    "denver",
    "detroit",
    "golden",
    "state",
    "houston",
    "indiana",
    "la",
    "los",
    "angeles",
    "memphis",
    "miami",
    "milwaukee",
    "minnesota",
    "new",
    "orleans",
    "york",
    "oklahoma"
    "city",
    "orlando",
    "philadelphia",
    "phoenix",
    "portland",
    "sacramento",
    "san",
    "antonio",
    "toronto",
    "utah",
    "washington",
    # Teams
    "hawks",
    "celtics",
    "nets",
    "hornets",
    "bulls",
    "cavaliers",
    "mavericks",
    "nuggets",
    "pistons",
    "warriors",
    "rockets",
    "pacers",
    "clippers",
    "lakers",
    "grizzlies",
    "heat",
    "bucks",
    "timberwolves",
    "hornets",
    "knicks",
    "thunder",
    "magic",
    "sixers",
    "suns",
    "trail",
    "blazers",
    "kings",
    "spurs",
    "raptors",
    "jazz",
    "wizards"
}


# TODO: continuously update game entity
# def update_game(game_status, value)


# find team names and scores from read data
def parse_output(words):
    output = []
    # TODO
    # game_status = GameStatus('', '', '', '')
    for word in words:
        if word.lower() in nba_teams:
            output.append(word.lower())
        elif word.isdigit():
            output.append(word)
        elif word.lower() in common_misreads:
            output.append(common_misreads[word.lower()])
    return output


def read_score(frame):
    text = pytesseract.image_to_string(Image.open(frame))
    words = text.split()
    output = parse_output(words)

    print(output)
