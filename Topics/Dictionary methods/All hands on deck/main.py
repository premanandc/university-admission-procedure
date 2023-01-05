NON_FACE_CARDS = 10
cards = [str(i) for i in range(2, NON_FACE_CARDS + 1)] + ['Jack', 'Queen', 'King', 'Ace']
deck = {card: i + 2 for i, card in enumerate(cards)}

print(sum([deck[input()] for _ in range(6)]) / 6)
