# -*- coding: utf-8 -*-

TEAM_NAME = "lauren_and_chun" #Pick a team name
MEMBERS = ["lmp3cn","ct5na"] #Include a list of your members’ UVA IDs

def get_connectFour(state):
    ourColor = state["your-token"]
    if ourColor == "R":
        theirColor = "Y"
    else:
        theirColor = "R"
    empty = True
    for i in range(0, state["columns"]):
        if len(state["board"][i]) != 0:
            empty = False
            break
    if empty == True:
        return {
            "move": state["columns"]/2,
            "team-code": state["team-code"]
        }

        #check horizontal to block
    max_rows = 0
    for i in range(0, state["columns"]):
        if len(state["board"][i]) > max_rows:
            max_rows = len(state["board"][i])

    countH = 0
    if state["columns"] >= state["connect_n"]:
        jcount = 0
        for j in range(0, max_rows):
            jcount += 1
            verCol = 0
            for k in range(0, state["columns"]):
                verCol += 1
                if len(state["board"][k]) >= jcount and state["board"][k][j] == theirColor :
                    countH += 1
                else:
                    countH = 0
                if countH == state["connect_n"] - 2 and len(state["board"][verCol + 1]) == jcount - 1:
                    return {
                        "move": verCol,
                        "team-code": state["team-code"]
                    }

    #if no horizontal, try to check vertical to block
    verCol = 0
    count = 0
    for i in range(0, state["columns"]):
        verCol += 1
        if len(state["board"][i]) >= state["connect_n"] - 1:
            for j in range(0, len(state["board"][i])):
                if state["board"][i][j] == theirColor:
                    count += 1
                else:
                    count = 0
        if count == state["connect_n"] - 1:
            return {
                "move": verCol,
                "team-code":state["team-code"]
            }


    #check diagonals here?


    # if nothing to block just go through all columns and put piece adjacent to one of our existing ones
    for i in range(0, state["columns"]):
        if i != 0 and i != state["columns"] -1:
            if abs(len(state["board"][i+1]) - len(state["board"][i])) <2:
                if state["board"][i+1][-1:] == ourColor:
                    return {
                        "move": i+1,
                        "team-code":state["team-code"]
                    }
            elif abs(len(state["board"][i-1]) - len(state["board"][i])) <2:
                    if state["board"][i-1][-1:] == ourColor:
                        return {
                            "move": i+1,
                            "team-code":state["team-code"]
                        }
            else:
                if len(state["board"][i]) > 1:
                    if state["board"][i][-2:] == ourColor:
                        return {
                        "move": i+1,
                        "team-code": state["team-code"]
                        }
        else:
            if i ==0:
                if abs(len(state["board"][i+1]) - len(state["board"][i])) <2:
                    if state["board"][i+1][-1:] == ourColor:
                        return {
                            "move": i+1,
                            "team-code":state["team-code"]
                        }
            else:
                if len(state["board"][i]) > 1:
                    if state["board"][i][-2:] == ourColor:
                        return {
                            "move": i+1,
                            "team-code": state["team-code"]
                        }
            if i == state["columns"]-1:
                if abs(len(state["board"][i-1]) - len(state["board"][i])) <2:
                    if state["board"][i-1][-1:] == ourColor:
                        return {
                            "move": i+1,
                            "team-code":state["team-code"]
                        }
            else:
                if len(state["board"][i]) > 1:
                    if state["board"][i][-2:] == ourColor:
                        return {
                            "move": i+1,
                            "team-code": state["team-code"]
                        }


    ######if nothing else works just drop in middle column.
    return {
        "move": int(state["columns"]/2),
        "team-code": state["team-code"]
    }

#hawk-dove game: our strategy is to play as a hawk
# and never swerve, giving a 100% win rate against doves
# and a 50% win rate against other hawks.
# https://en.wikipedia.org/wiki/Chicken_(game)
def get_chicken_move(state):
    return {
        "move": 0,
        "team-code": state["team-code"]
    }
def get_move(state):
    if state["game"] == "chicken":
        return get_chicken_move(state)
    if state["game"] == "connect_more":
        return get_connectFour(state)
'''
# for testing
state = {
    "team-code": "eef8976e",
    "game": "connect_more",
    "opponent-name": "mighty_ducks",
    "columns": 8,
    "connect_n": 5,
    "your-token": "R",
    "board": [
        [],
        ["R", "Y"],
        ["R","Y"],
        ["Y","Y"],
        ["Y"],
        [],
        [],
        []
    ]
}
print(get_move(state))
'''