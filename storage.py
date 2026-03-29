import time

users = {}

FREE_TRIAL_SECONDS = 86400  # 1 day

def start_trial(user_id):
    users[user_id] = {
        "trial_start": time.time(),
        "paid": False
    }

def activate_paid(user_id):
    users[user_id] = {
        "paid": True
    }

def is_premium(user_id):
    user = users.get(user_id)

    if not user:
        return False

    if user.get("paid"):
        return True

    if "trial_start" in user:
        if time.time() - user["trial_start"] < FREE_TRIAL_SECONDS:
            return True

    return False

def has_used_trial(user_id):
    return user_id in users
