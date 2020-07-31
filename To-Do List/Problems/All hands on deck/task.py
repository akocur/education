rank_cards = {f'{rank}': rank for rank in range(2, 11)}
face_cards = 'Jack', 'Queen', 'King', 'Ace'
rank_cards.update({f'{face_cards[rank - 11]}': rank for rank in range(11, 15)})
print(sum(rank_cards[input()] for _ in range(6)) / 6)
