from telegram import LabeledPrice

PRICE = 300

def get_prices():
    return [LabeledPrice("Lifetime Access", PRICE)]
