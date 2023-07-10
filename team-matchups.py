# Michael L. Kelley Jr.
# June 26, 2023
# team-matchups.py
# Print all of the possible matchups between teams
# Take into consideration home + away status

teams = ['Dragons', 'Bears', 'Pandas', 'Unicorns']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
            
              