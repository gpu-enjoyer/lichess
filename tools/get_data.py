
import chess.pgn
import requests
from   pathlib import Path


url     =  "https://lichess.org/api/games/user/qorovin"
headers = {"Accept": "application/x-chess-pgn"}
params  = {
    "perfType": "blitz",
    "rated":    "true",
    "clocks":   "true",
    "opening":  "true"
}

response = requests.get(url, params=params, headers=headers)


folder = Path(__file__).parent

with open(folder / "__data.pgn", "w") as f:
    f.write(response.text)


games  = []

with open(folder / "__data.pgn", "r") as f:
    while True:
        game = chess.pgn.read_game(f)
        if game is None:
            break
        if game.headers.get("TimeControl") != "300+3":
            continue
        games.append(game)


with open(folder / "../data.pgn", "w") as out:
    for game in games:
        print(game, file=out)
        print(file=out)
