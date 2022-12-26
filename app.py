from constants import TEAMS, PLAYERS

def clean_data():
    cleaned_data = []
    for teamPlayer in PLAYERS:
        teamPlayer['height'] = int(teamPlayer['height'][:2]) # remove the 'in' from the height
        teamPlayer['experience'] = True if teamPlayer['experience'] == 'YES' else False # convert to boolean
        teamPlayer['guardians'] = teamPlayer['guardians'].split(' and ') # split the guardians into a list
        cleaned_data.append(teamPlayer)
    return cleaned_data


def balance_teams(TEAMS, PLAYERS):
    teamPlayers = {}
    for team in TEAMS:
        teamPlayers[team] = []
    #balance players betweeen teams
    for player in PLAYERS:
        if len(teamPlayers[TEAMS[0]]) > len(teamPlayers[TEAMS[1]]):
            teamPlayers[TEAMS[1]].append(player)
        elif len(teamPlayers[TEAMS[1]]) > len(teamPlayers[TEAMS[2]]):
            teamPlayers[TEAMS[2]].append(player)
        else:
            teamPlayers[TEAMS[0]].append(player)
    return teamPlayers

def join_names_from_teams(team):
    namesInString = ''
    for player in balancedTeams[team]:
        namesInString += player['name'] + ', '
    return namesInString[:-2] # remove the last comma and space

def print_team(team):
    no_of_experienced_players = 0
    no_of_inexperienced_players = 0
    total_height = 0
    guardians = []

    for team_member in balancedTeams[team]:
        if team_member['experience']:
            no_of_experienced_players += 1
        else:
            no_of_inexperienced_players += 1
        total_height += team_member['height']
        guardians += team_member['guardians']

    average_height = total_height / len(balancedTeams[team])

    print(f'Team: {team} Stats')
    print('--------------------')
    print('Total players: ', len(balancedTeams[team]))
    print('Players on team: ', join_names_from_teams(team) + '\n')
    print(f'Experienced players: {no_of_experienced_players}')
    print(f'Inexperienced players: {no_of_inexperienced_players}')
    print(f'Average height: {average_height}')
    print(f'Guardians: {", ".join(guardians)}\n')


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
            raise Exception('Invalid input, please try again \n')
    except ValueError:
        print('Invalid input, please try again \n')
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