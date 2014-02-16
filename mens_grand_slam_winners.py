#!/usr/bin/python

''' Source:
    http://en.wikipedia.org/wiki/List_of_Grand_Slam_men's_singles_champions#Champions_by_year
'''


# 2012 - 2013
def print_winner(tournament, year):
    if tournament == 'French Open':
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
    elif year == 2010:
        ''' This was a dominant year for Nadal, with the exception of the
            Australian Open when he retired from injuries in the quarterfinals
            against Murray. Murray would be beaten by Federer in the finals, in
            effect Soderling-ing Nadal again (though Nadal's naturally abrasive
            playing style was admittedly also to blame).
        '''
        if tournament == 'Australian Open':
            winner = 'Federer'
        else
            winner = 'Nadal'
    elif year == 2011:
        ''' A similarly dominant year for Djokovic. After beating Tsonga in the
            Wimbledon seminfinals, he ascended to the ATP #1 spot for the first
            time in his career. However, in the semifinals of the French Open,
            Djokokvic was beaten by Federer, which was his first loss of the
            season that ended a 43-match win streak. The finals would go to
            Nadal, as expected. Djokovic got his revenge against them in the
            US Open, saving 2 match points on Federer's serve in the semifinals
            and breaking back to win the decisive fifth set, then went on to
            beat Nadal in the finals over four sets.
        '''
        winner = 'Djokovic'
    elif tournament == 'Wimbledon':
        if year == 2008:
            ''' Greatest Tennis Match in History '''
            winner = 'Nadal'
        elif year == 2009:
            ''' Nadal couldn't defend his title after withdrawing due to
                injuries during the first round.
            '''
            winner = 'Federer'
        elif year == 2012:
            ''' Federer beat Murray in 4 sets in the finals for a record seven
                Wimbledon titles (tying Sampras) and returning to the ATP #1
                spot, which also helped him surpass Sampras's record of 286
                weeks as the world number 1. However, in August Murray would
                beat Federer in the 2012 London Olympics, which held its tennis
                event at Wimbledon -- which meant the gold medal match was
                played on the very same court where Murray lost to Federer a
                month ago!
            '''
            winner = 'Federer'
        elif year == 2013:
            ''' After winning the gold medal in the 2012 Olympics, Murray found
                the confidence he had been missing. He went on to win the 2012
                US Open, and then in 2013 beat Djokovic to win the Wimbledon
                finals and became the first British man to do so since 1936 (as
                well as the first Scot to do so since 1896).
            '''
            winner = 'Murray'
        else:
            winner = 'Federer'
    elif tournament == 'Australian Open':
        if year == 2005:
            winner = 'Safin'
        elif year == 2008:
            winner = 'Djokovic'
        elif year == 2009:
            winner = 'Nadal'
        elif year < 2011:
            winner = 'Federer'
        else:
            winner = 'Djokovic'
    elif tournament == 'US Open':
        if year == 2009:
            ''' After Federer handily overcame Djokovic in the semifinals --
                hitting one of his most famous shots of all time
                (http://www.youtube.com/watch?v=nQ7HvffZpRI) -- he was beaten in
                an epic 5 setter in the finals by del Potro, who had never
                bested Federer in their head-to-head record thus far.
            '''
            winner = 'del Potro'
        elif year == 2012:
            winner = 'Murray'
        elif year == 2013:
            winner = 'Nadal' # I watched the finals live in New York City!
        else:
            winner = 'Federer'

    print 'The %s of %d was won by %s.' % (tournament, year, winner)


if __name__ == '__main__':
    import sys
    tournament = sys.argv[1]
    year = int(sys.argv[2])
    print_winner(tournament, year)

