def calculate_points(results):
    points = {}
    for result in results:
        team1, team2, score1, score2 = result
        if score1 > score2:
            points[team1] = points.get(team1, 0) + 3
        elif score1 < score2:
            points[team2] = points.get(team2, 0) + 3
        else:
            points[team1] = points.get(team1, 0) + 1
            points[team2] = points.get(team2, 0) + 1
    return points

def calculate_goals(results):
    goal_difference = {}
    for result in results:
        team1, team2, score1, score2 = result
        goal_difference[team1] = goal_difference.get(team1, 0) + score1 - score2
        goal_difference[team2] = goal_difference.get(team2, 0) + score2 - score1
    return goal_difference

def sort_teams(teams):
    return sorted(teams, key=lambda x: (-teams[x]["points"], -teams[x]["wins"], -teams[x]["goal_difference"], x))

results = []
teams = {}
team_names = ['Iran','Spain','Portugal','Morocco']

for i in range(len(team_names)):
    teams[team_names[i]] = {"wins": 0, "draws": 0, "losses": 0, "goal_difference": 0, "points": 0}

for i in range(len(team_names)):
    for j in range(i + 1, len(team_names)):
        match_result = input().strip()
        score1, score2 = map(int, match_result.split('-'))
        results.append((team_names[i], team_names[j], score1, score2))

for result in results:
    team1, team2, score1, score2 = result
    if score1 > score2:
        teams[team1]["wins"] += 1
        teams[team2]["losses"] += 1
    elif score1 < score2:
        teams[team2]["wins"] += 1
        teams[team1]["losses"] += 1
    else:
        teams[team1]["draws"] += 1
        teams[team2]["draws"] += 1

points = calculate_points(results)
goal_difference = calculate_goals(results)

for team in teams:
    teams[team]["points"] = points.get(team, 0)
    teams[team]["goal_difference"] = goal_difference.get(team, 0)

sorted_teams = sort_teams(teams)

for team in sorted_teams:
    print(f"{team} wins:{teams[team]['wins']} , losses:{teams[team]['losses']} , draws:{teams[team]['draws']} , goal difference:{teams[team]['goal_difference']} , points:{teams[team]['points']}")