#!/usr/bin/env python3
# coding: utf-8

class Football_Team():
    def __init__(self, name, win, lose, draw):
        self.name = name
        self.win = win
        self.lose = lose
        self.draw = draw
    
    def calc_win_rate(self):
        return self.win / (self.win + self.lose)

    def show_team_result(self):
        print(f'{self.name:12s} {self.win:3d}{self.lose:3d} {self.draw:2d} {self.calc_win_rate():.3f}')


def main():
    pass

if __name__ == '__main__':
    main()