students = int(input())
teams = int(input())
each_team = students // teams
left_out = students % teams

print("The number of students in each team is", each_team, "and left out is", left_out)