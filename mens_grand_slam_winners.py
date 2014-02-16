#!/usr/bin/python

''' Source:
    http://en.wikipedia.org/wiki/List_of_Grand_Slam_men's_singles_champions#Champions_by_year
'''


# 2008
def print_winner(tournament, year):
    if tournament == 'Wimbledon' and year == 2008:
        ''' Greatest Tennis Match in History '''
        winner = 'Nadal'
    elif tournament == 'French Open':
        if year == 2004:
            winner = 'Gaudio'
        else:
            winner = 'Nadal'
    elif tournament == 'Australian Open':
        if year == 2005:
            winner = 'Safin'
        elif year == 2008:
            winner = 'Djokovic'
        else:
            winner = 'Federer'
    else:
        winner = 'Federer'

    print 'The %s of %d was won by %s.' % (tournament, year, winner)


if __name__ == '__main__':
    import sys
    tournament = sys.argv[1]
    year = int(sys.argv[2])
    print_winner(tournament, year)

