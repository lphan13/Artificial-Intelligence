TEAM_NAME = "lauren_and_chun" #Pick a team name
MEMBERS = ["lmp3cn","ct5na"] #Include a list of your members' UVA IDs

# for testing purposes only; REMOVE WHEN READY TO SUBMIT
saved = {
    "prev-payoffs": [
        27,
        21,
        35,
        20,
        79,
        33,
        42,
        39,
        80,
        25,
        24,
        9,
        62,
        44,
        43,
        10,
        67,
        77,
        2,
        80,
        11,
        53,
        77,
        51,
        8,
        83,
        20,
        74,
        12,
        18,
        15,
        78,
        87,
        38,
        86,
        57,
        94,
        87,
        48,
        99,
        68,
        29,
        22,
        34,
        45,
        76,
        29,
        46,
        57,
        14,
        5,
        52,
        69,
        90,
        40,
        72,
        51,
        47,
        48,
        92,
        40,
        91,
        38,
        66,
        56,
        99,
        78,
        27,
        4,
        61,
        68,
        56,
        21,
        57,
        31,
        42,
        70,
        71,
        89,
        86,
        84,
        21,
        77,
        94,
        48,
        15,
        31,
        37,
        30,
        85,
        4,
        74,
        52,
        6,
        10,
        18,
        88,
        61,
        100,
        85
    ],
    "want-slots": [98,45,20],
    "want-payoffs": [30,80,120]

}
def load_info():
    return saved

def save_info(info):
    saved = info
# for testing purposes only; REMOVE WHEN READY TO SUBMIT

def move_bandit(state):

    loaded_info = load_info()
    if state["pulls-left"] == 10000:
        print(0)
        return {
            "team-code": state["team-code"],
            "game": "phase_1",
            "pull": 0
        }
    else:
        #load the previous move into our load data
        if state["last-cost"]:
            loaded_info.setdefault("prev-payoffs",[]).append(state["last-cost"])
            save_info(loaded_info)
        #if haven't explored all slots, try all possible slot machines and save them
        if state["pulls-left"] > 9900:
            currPull = 10000 - state["pulls-left"]
            print(currPull)
            return {
            "team-code": state["team-code"],
            "game": "phase_1",
            "pull": currPull
            }
        else:
            #iterate through the array and find which one is the best slot to choose- then keep picking it
            max = 0
            for i in range(len(loaded_info["prev-payoffs"])):
               if loaded_info["prev-payoffs"][i] > max:
                   max = i
            print(max)
            return {
                "team-code": state["team-code"],
                "game": "phase_1",
                "pull": max
            }
def move_auction1(state):

    #load data from phase 1 - can see all payoffs from all slots
    loaded_info = load_info()
    want = []
    want_payoffs = []
    max = 0
    for i in range(0,10):
        for j in range(0, 100):
            if loaded_info["prev-payoffs"][j] > max and j not in want:
                max = j
        # add top 10 auction choices
        want.append(max)
        want_payoffs.append(loaded_info["prev-payoffs"][max])
        max = 0
    loaded_info.setdefault("want-slots",[]).append(want)
    loaded_info.setdefault("want-payoffs",[]).append(want_payoffs)
    save_info(loaded_info)
    print(loaded_info)
    return {
        "team-code": state["team-code"],
        "game": "phase_2_a",
        "auctions": want
    }
def move_auction2(state):
    loaded_info = load_info()
    if state["auction-number"] in loaded_info["want-slots"]:
        ind = loaded_info["want-slots"].index(state["auction-number"])
        payoff_per_pull = loaded_info["want-payoffs"][ind]
        bid = (payoff_per_pull * 10000) * .70
    else:
        bid = 0
    return {
        "team-code": state["team-code"],
        "game": "phase_2_b",
        "bid": bid
    }
def get_move(state):
    if state["game"] == "phase_1":
        return move_bandit(state)
    if state["game"] == "phase_2_a":
        return move_auction1(state)
    if state["game"] == "phase_2_b":
        return move_auction2(state)

#for testing
state = {
    "team-code": "eef8976e",
    "game": "phase_2_b",
    "auction-number": 20,
    "your-slots": [],
}
get_move(state)