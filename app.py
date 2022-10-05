from os import stat
from constants import TEAMS, PLAYERS

def clean_data():
    cleaned_data = []
    for teamPlayer in PLAYERS:
        teamPlayer['height'] = int(teamPlayer['height'][:2]) # remove the 'in' from the height
        teamPlayer['experience'] = True if teamPlayer['experience'] == 'YES' else False # convert to boolean
        cleaned_data.append(teamPlayer)
    return cleaned_data


def balance_teams(TEAMS, PLAYERS):
    teamPlayers = {'Panthers': [], 'Bandits': [], 'Warriors': []}
    for player in PLAYERS:
        
        if len(teamPlayers['Panthers']) > len(teamPlayers['Bandits']): 
            # if team 1 has more players than team 2
            teamPlayers['Bandits'].append(player)
        
        elif len(teamPlayers['Bandits']) > len(teamPlayers['Warriors']): 
            # if team 2 has more players than team 3
            teamPlayers['Warriors'].append(player)
        
        else:
            teamPlayers['Panthers'].append(player)    
            # if team 1 has less players than team 2 and team 3
    return teamPlayers

def join_names_from_teams(team):
    namesInString = ''
    for player in balancedTeams[team]:
        namesInString += player['name'] + ', '
    return namesInString[:-2] # remove the last comma and space

def print_team(team):
    print(f'Team: {team} Stats')
    print('--------------------')
    print('Total players: ', len(balancedTeams[team]))
    print('Players on team: ', join_names_from_teams(team) + '\n')

def menu():
    print('Basketball Team Statistics Tool')
    print('--------------------')
    print('A) Display Team Statistics')
    print('B) Exit \n')

    menuChoice = input('Enter an option : \n')
    if menuChoice.lower() == 'a':
        stats_menu()
    elif menuChoice.lower() == 'b':
        print('Exiting...')
        exit()
    else:
        print('Incorrect input, please try again \n')
        menu()


def stats_menu():
    print(f'A: {TEAMS[0]} Statistics')
    print(f'B: {TEAMS[1]} Statistics')
    print(f'C: {TEAMS[2]} Statistics')
    print(f'D: Exit')
    try:
        statsChoice = input('Enter an option: \n')
        if statsChoice.lower() not in ['a', 'b', 'c', 'd']:
            raise Exception('#Incorrect input, please try again \n')
    except ValueError:
        print('Incorrect input, please try again \n')
        stats_menu()
    except Exception as err:
        print(err)
        stats_menu()
    else:
        if statsChoice.lower() == 'a':
            print_team(TEAMS[0])
            stats_menu()
        elif statsChoice.lower() == 'b':
            print_team(TEAMS[1])
            stats_menu()
        elif statsChoice.lower() == 'c':
            print_team(TEAMS[2])
            stats_menu()
        elif statsChoice.lower() == 'd':
            print('Exiting...')
            exit()

def start_game():
    menu()

if __name__ == '__main__':
    cleanedData = clean_data()
    balancedTeams = balance_teams(TEAMS, cleanedData)
    start_game()