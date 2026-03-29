from telegram import LabeledPrice

PREMIUM_TITLE = "IPLClaw Lifetime 💀"
PREMIUM_DESC = "Ball-by-ball roasting + paisa vasool insights"

PRICE_STARS = 300

def get_prices():
    return [LabeledPrice("Lifetime Access", PRICE_STARS)]
