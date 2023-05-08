import sqlite3
import time


def add_user(user_id, first_name, last_name, username):
    conn = sqlite3.connect('karma.db')
    cur = conn.cursor()
    m = [user_id, first_name, last_name, username]
    cur.execute('INSERT INTO users VALUES (?, ?, ?, ?)', m)
    m = [user_id, 0]
    cur.execute('INSERT INTO karma_rate VALUES (?, ?)', m)
    conn.commit()
    cur.close()
    conn.close()


def user_search(user_id):
    conn = sqlite3.connect('karma.db')
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users WHERE user_id = ?;", [user_id])
    all_results = cur.fetchall()
    if all_results:
        res = 'ok_user'
    else:
        res = 'no_user'
    cur.close()
    conn.close()
    return res


def user_rate(user_id):
    conn = sqlite3.connect('karma.db')
    cur = conn.cursor()
    cur.execute("SELECT rate FROM karma_rate WHERE user_id = ?;", [user_id])
    all_results = cur.fetchall()
    cur.close()
    conn.close()
    return all_results


def add_action(user_id, action, rate, from_user, user_msg_id, user_msg, from_user_msg_id, from_user_msg):
    conn = sqlite3.connect('karma.db')
    cur = conn.cursor()
    date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    m = [user_id, action, rate, from_user, user_msg_id, user_msg, from_user_msg_id, from_user_msg, date_time]
    cur.execute('INSERT INTO karma_history VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', m)
    m = [user_rate(user_id)+rate, user_id]
    cur.execute('UPDATE karma_rate SET rate = ? WHERE user_id = ?', m)
    conn.commit()
    cur.close()
    conn.close()
