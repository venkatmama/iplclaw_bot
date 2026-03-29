import os
import time
import psycopg

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(DATABASE_URL, autocommit=True)

def create_table():
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            trial_start BIGINT,
            is_paid BOOLEAN DEFAULT FALSE
        )
        """)

def add_user_if_not_exists(user_id):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO users (user_id, trial_start, is_paid)
        VALUES (%s, %s, FALSE)
        ON CONFLICT (user_id) DO NOTHING
        """, (user_id, int(time.time())))

def activate_paid(user_id):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE users SET is_paid = TRUE WHERE user_id = %s
        """, (user_id,))

def is_premium(user_id):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT trial_start, is_paid FROM users WHERE user_id = %s
        """, (user_id,))
        row = cur.fetchone()

        if not row:
            return False

        trial_start, is_paid = row

        if is_paid:
            return True

        if trial_start:
            if time.time() - trial_start < 86400:
                return True

        return False

def has_user(user_id):
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))
        return cur.fetchone() is not None
