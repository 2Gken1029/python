#!/usr/bin/env python3
# coding: utf-8

from football_team import Football_Team

brazil = Football_Team('Brazil', 73, 18, 18)
italy = Football_Team('Italy', 45, 21, 21)
argentina = Football_Team('Argentina', 43, 15, 15)
westgermany = Football_Team('West_Germany', 36, 14, 14)
france = Football_Team('France', 34, 13, 13)
germany = Football_Team('Germany', 31, 6, 6)
spanish = Football_Team('Spanish', 30, 15, 15)

teams = [brazil, italy, argentina, westgermany, france, germany, spanish]
for team in teams:
    team.show_team_result()

print(team.show_team_result())

if __name__ == '__main__':
    pass