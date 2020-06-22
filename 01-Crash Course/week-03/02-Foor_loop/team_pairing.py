team = ['varun', 'abhinav', 'suman', 'gaurav']

for home_team in team:
    for opponent in team:
        if home_team != opponent:
            print(home_team + " vs " + opponent)