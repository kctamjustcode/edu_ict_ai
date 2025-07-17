import random, copy
from collections import Counter

# assuming infinite number of cards
# no special rules, e.g. split, pair, 5 cards etc. (and no blackjack)

cards = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']
nums = [0] + list(range(2, 11)) + [10, 10, 10]


def is_blackjack(cardset):
    return 'A' in player_cards and ('10' in player_cards or 'J' in player_cards or 'Q' in player_cards or 'K' in player_cards)

'''
dealer_cards = []
dealer_cards += [cards[random.randint(0, 12)]]
dealer_cards += [cards[random.randint(0, 12)]]
'''
tests = 5
for _ in range(tests):
    trials = 1000
    stops = 0
    stat = []
    init = []

    for _ in range(trials):
        player_cards = []
        player_cards += [cards[random.randint(0, 12)]]
        player_cards += [cards[random.randint(0, 12)]]
        #print(player_cards)
        stopped = False
        while not stopped:
            if 'A' in player_cards:
                #player_cards_cp = copy.deepcopy(player_cards)
                #player_cards_cp.remove('A')
                points = sum( [ nums[cards.index(player_cards[i])] for i in range(len(player_cards)) ] )
                if 16 <= points <= 20:
                    stopped = True
                    #print('1', points, player_cards)
                    stops += 1
                    stat += [str(points+1)]
                    init += [tuple(sorted(player_cards[:2]))]
                elif 6 <= points <= 10:
                    stopped = True
                    #print('11', points, player_cards)
                    stops += 1
                    stat += [str(points+11)]
                    init += [tuple(sorted(player_cards[:2]))]
                elif points > 21:
                    stopped = True
                    #print('bushed')
                else:
                    player_cards += [cards[random.randint(0, 12)]]
            else:
                #player_cards_cp = copy.deepcopy(player_cards)
                points = sum( [ nums[cards.index(player_cards[i])] for i in range(len(player_cards)) ] )
                if 17 <= points <= 21:
                    stopped = True
                    #print('normal', points, player_cards)
                    stops += 1
                    stat += [str(points)]
                    init += [tuple(sorted(player_cards[:2]))]
                elif points > 21:
                    stopped = True
                    #print('bushed')
                else:
                    player_cards += [cards[random.randint(0, 12)]]

    print(stops/trials)
    print(Counter(init))
    print(Counter(stat))    
