import random

# Construct the deck

card_deck = ['wild', 'wild', 'wild', 'wild', 'd4', 'd4', 'd4', 'd4']

for colour in ['r', 'g', 'b', 'y']:
	for num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'skip', 'reverse', 'd2']:
		card = colour + '_' + num
		card_deck.append(card)

for colour in ['r', 'g', 'b', 'y']:
	for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'skip', 'reverse', 'd2']:
		card = colour + '_' + num
		card_deck.append(card)

# Shuffling

random.shuffle(card_deck)


p1 = card_deck[:7]
p2 = card_deck[7:14]
p3 = card_deck[14:21]
p4 = card_deck[21:28]

discard_deck = card_deck[28:]

while(1):
	opt1:
		p1.append(discard_deck[0])
		discard_deck.pop(0)
	opt2:
		play p1[card]
		if p1[card][0] == discard_deck[0][0] or (p1[card][0] == w or p1[card] == 'd4')