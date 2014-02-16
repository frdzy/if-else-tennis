#!/usr/bin/python

''' Source:
    http://en.wikipedia.org/wiki/List_of_Grand_Slam_men's_singles_champions#Champions_by_year
'''


# 2009
def print_winner(tournament, year):
    if tournament == 'Wimbledon':
        if year == 2008:
            ''' Greatest Tennis Match in History '''
            winner = 'Nadal'
        else:
            ''' Nadal couldn't defend his title after withdrawing due to
                injuries during the first round.
            '''
            winner = 'Federer'
    elif tournament == 'French Open':
        if year == 2004:
            winner = 'Gaudio'
        elif year == 2009:
            ''' The term "Soderlinged" was coined after the man who went up
                against Nadal in the fourth round and played a phenomenal match
                to pull off a tremendous upset. Soderling would eventually go on
                to reach the finals, only to lose to Federer. To date, this
                remains the only year Federer claimed the French Open title, as
                well as the only loss for Nadal at the French Open **since his
                debut in 2005**.
            '''
            winner = 'Federer'
        else:
            winner = 'Nadal'
    elif tournament == 'Australian Open':
        if year == 2005:
            winner = 'Safin'
        elif year == 2008:
            winner = 'Djokovic'
        elif year == 2009:
            winner = 'Nadal'
        else:
            winner = 'Federer'
    elif tournament == 'US Open':
        if year == 2009:
            ''' After Federer handily overcame Djokovic in the semifinals --
                hitting one of his most famous shots of all time
                (http://www.youtube.com/watch?v=nQ7HvffZpRI) -- he was beaten in
                an epic 5 setter in the finals by del Potro, who had never
                bested Federer in their head-to-head record thus far.
            '''
            winner = 'del Potro'
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

