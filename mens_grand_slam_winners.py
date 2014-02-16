#!/usr/bin/python

''' Source:
    http://en.wikipedia.org/wiki/List_of_Grand_Slam_men's_singles_champions#Champions_by_year
'''


# 2004 - 2007
def print_winner(tournament, year):
    if tournament == 'French Open':
        if year == 2004:
            winner = 'Gaudio'
        else:
            winner = 'Nadal'
    elif tournament == 'Australian Open' and year == 2005:
        winner = 'Safin'
    else:
        winner = 'Federer'

    print 'The %s of %d was won by %s.' % (tournament, year, winner)


if __name__ == '__main__':
    import sys
    tournament = sys.argv[1]
    year = int(sys.argv[2])
    print_winner(tournament, year)

