"""

https://www.codewars.com/kata/5b75aa794eb8801bd0000033/python

"""
import unittest


class RummyTest(unittest.TestCase):
    def test_simple(self):
        config = [
            ("Single Runs: Aces run with J", "5♠ K♥ K♣ Q♥ A♠ J♥ A♥", 19),
            ("Single Runs: Aces run", "5♠ K♥ K♣ Q♥ A♠ T♦ A♥", 29),
            ("Multiple Melds: Get Score", 'A♠ 2♠ 3♠ 3♦ 3♥ 4♠ 5♠', 6),
            ("Single Runs: Get Score", '7♦ 6♦ 8♦ A♣ 2♥ 5♥ 6♠', 14),
            ("Single Set: Get Score", '3♠ 3♦ 3♥ 4♥ 8♦ J♠ K♠', 36),
            ("Two Melds: Get Score", '5♠ 5♦ 5♥ 7♥ 8♥ 9♥ 2♥', 2),

            ("Hand sets", 'A♦ A♣ A♠ 2♣ 2♠ 2♥ 2♦', 0),
            ("Hand runs", 'A♣ 2♣ 3♣ 4♣ 9♠ T♠ J♠', 0),
            ("Hand set and run", '3♠ 3♥ 3♦ 5♠ 6♠ 7♠ 8♠', 0),
            ("Crossover", '3♠ 3♥ 3♦ A♣ 2♣ 3♣ 4♣', 0),
        ]

        for title, h, exp in config:
            hand = Hand(h.split())
            self.assertEqual(hand.get_score(), exp)

    def test_discard_card(self):
        config = [
            ('5♠ 4♠ 3♣ 8♠ 5♦ 6♠ 3♦', 'A♥', 12, '8♠'),  # (startng hand, added card, final score, best possible discard)
            ('5♦ 8♣ 3♥ 6♦ 4♥ 9♥ 8♦', 'Q♠', 43, 'Q♠'),
            ('5♥ 3♥ A♥ 8♥ 6♣ 2♠ 5♦', '4♦', 26, '8♥'),
            ('3♥ 2♦ 4♥ 4♠ A♠ 3♦ A♥', 'K♥', 18, 'K♥'),
            ('5♦ 6♠ 2♣ 2♥ 5♣ 8♥ 6♥', 'J♠', 34, 'J♠'),
        ]

        for h, toAdd, score, bestDiscard in config:
            hand = Hand(h.split())
            actDiscard = hand.add_card(toAdd)
            actHand = hand.get_hand()
            actScore = hand.get_score()
            expHand = [c for c in h.split() + [toAdd] if c != bestDiscard]
            self.assertIn(actDiscard, bestDiscard)
            self.assertEqual(hand.get_hand(), expHand)
            self.assertEqual(hand.get_score(), score)


import itertools


RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
RANK_VALUE = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
              'J': 11, 'Q': 12, 'K': 13}


class Card:
    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return RANK_VALUE[self.rank]

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @classmethod
    def parse(cls, c):
        return Card(c[0], c[1])

    def __repr__(self):
        return "{}{}".format(self.rank, self.suit)

    def __hash__(self):
        return hash(self.__str__())


class Hand:
    @property
    def cards(self):
        return self._cards

    def __init__(self, cards_lst):
        self._cards = []
        for card in cards_lst:
            self.cards.append(Card.parse(card))

    def get_hand(self):
        return [str(card) for card in self.cards]

    def find_sets(self):
        buckets = dict()
        for card in self.cards:
            if card.value not in buckets:
                buckets[card.value] = []
            buckets[card.value].append(card)

        result = []
        for b in buckets.values():
            if len(b) < 3:
                continue
            if len(b) == 3:
                result.append(b)
                continue

            result.append(b)
            for sb in itertools.combinations(b, 3):
                result.append(sb)

        return result

    def find_runs(self):
        buckets = dict()
        for card in self.cards:
            if card.suit not in buckets:
                buckets[card.suit] = []
            buckets[card.suit].append(card)

        result = []
        for suit in buckets:
            buckets[suit] = sorted(buckets[suit], key=lambda c: c.value)
            for i in range(len(buckets[suit])):
                run = [buckets[suit][i]]
                while i < len(buckets[suit]) - 1 and buckets[suit][i].value + 1 == buckets[suit][i + 1].value:
                    run.append(buckets[suit][i + 1])
                    i += 1

                    if len(run) > 2:
                        result.append(run[:])

                    if len(run) >= 2 and buckets[suit][0].rank == 'A' and run[-2].rank == 'Q' and run[-1].rank == 'K':
                        run.append(buckets[suit][0])
                        result.append(run[:])
                        run.pop()
        return result

    def get_score(self):
        all_melds = [set(h) for h in self.find_sets() + self.find_runs()]
        if not all_melds:
            return sum([c.value for c in self.cards])

        min_score = None
        for i, meld in enumerate(all_melds):
            score = sum([c.value for c in self.cards if c not in meld])
            if min_score is None or score < min_score:
                min_score = score
            for j in range(i+1, len(all_melds)):
                if meld.isdisjoint(all_melds[j]):
                    score = sum([c.value for c in self.cards if c not in meld | all_melds[j]])
                    if min_score is None or score < min_score:
                        min_score = score

        return min_score

    def add_card(self, c):
        new_card = Card.parse(c)
        discard_card = None
        min_score = None
        min_idx = None

        self.cards.append(new_card)
        for i, card in enumerate(self.cards):
            self.cards.pop(i)
            score = self.get_score()
            if min_score is None or score < min_score:
                min_score = score
                discard_card = str(card)
                min_idx = i
            self.cards.insert(i, card)

        self.cards.pop(min_idx)

        return discard_card


if __name__ == "__main__":
    unittest.main()