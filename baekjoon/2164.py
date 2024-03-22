#  큐

N = int(input())
cards = [ i for i in range(1, N+1) ]

while len(cards) != 1:
    # 한 사이클 돌린 결과
    even_cards = cards[1::2]
    if len(cards) % 2:
        cards = [cards[-1]] + even_cards
    else:
        cards = even_cards

print(cards[0])