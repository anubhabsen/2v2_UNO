card_deck = ['wild', 'wild', 'wild', 'wild', 'd4', 'd4', 'd4', 'd4']

for colour in ['red', 'green', 'blue', 'yellow']:
	for num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'skip', 'reverse', 'd2']:
		card = colour + '_' + num
		card_deck.append(card)

for colour in ['red', 'green', 'blue', 'yellow']:
	for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'skip', 'reverse', 'd2']:
		card = colour + '_' + num
		card_deck.append(card)

print card_deck