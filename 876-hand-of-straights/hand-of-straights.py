class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_counts = {}
        for card in hand:
            card_counts[card] = card_counts.get(card, 0) + 1

        while card_counts:
            first_card = min(card_counts.keys())
            for i in range(first_card, first_card + groupSize):
                if not i in card_counts:
                    return False
                card_counts[i] -= 1
                if not card_counts[i]:
                    del card_counts[i]
        return True
