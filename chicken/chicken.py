TEAM_NAME = "????" #Pick a team name
MEMBERS = ["lmp3cn","ct5na"] #Include a list of your members’ UVA IDs
'''
INFO FORMAT: 

info = {
    "past-reaction-times": [],
    "player-behavior": {
        "player1": [],
        "player2": []
    }
}
save_data(info)
loaded_info = load_data() #Would be silly to load just after saving, just including this
as example of call
'''
def get_move(state):
    #info = load_data()
    return {
        "move": 0,
        "team-code": "lmp3cn,ct5na"
    }