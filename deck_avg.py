import logging
import os
import sys

import pprint

def extract_cards(decklist):
    deck = {'main': {}, 'sideboard': {}}
    is_sideboard = False
    for line in decklist.split('\n'):
        if 'sideboard' in line.lower():
            is_sideboard = True
        else:
            temp = line.split(' ')
            deck['sideboard' if is_sideboard else 'main'][' '.join(temp[1:])] = int(temp[0])
    return deck

def main(path):
    decks = []
    for root, dirs, files in os.walk(path):
        for file_ in files:
            with open(os.path.join(root, file_), 'r') as deckfile:
                decks.append(extract_cards(deckfile.read().strip()))

    for deck in decks:
        pprint.pprint(deck)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='Input dir of MTGO files')

    args = parser.parse_args()

    if os.path.exists(args.dir):
        main(args.dir)
    else:
        logging.error('Path not found: {}'.format(args.dir))
        sys.exit(1)
