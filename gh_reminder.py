import pgi
import datetime
import time
import math
import gh_contributions
import threading
from pgi.repository import Notify

Notify.init('Github Streak Reminder')

checked_hours = []
commited_today = False

def send_reminder(title, message, urgency):
    n = Notify.Notification.new(title, message, 'dialog-information')
    n.set_urgency(urgency)
    n.show()


def min_until_midnight():
     now = datetime.datetime.now()
     tomorrow = datetime.datetime(now.year, now.month, now.day) + \
                datetime.timedelta(1)
     return math.floor(abs(tomorrow - now).seconds / 60)

def CheckContibutions():
    global checked_hours
    global commited_today

    timestamp = datetime.datetime.now().time()

    # Fix. This checks if it's the first hour of the day.
    # If it detects this it checks if there are more then 1 checked hour
    # if so it clears it. it needs to be higher then 1 or else it keeps clearing
    if timestamp.hour == 0 and len(checked_hours) > 1:
        checked_hours = []
        commited_today = False

    if (((timestamp.hour in checked_hours) and timestamp.hour != 23) or commited_today == True):
        t = threading.Timer(60, CheckContibutions)
        t.start()
        return

    checked_hours.append(timestamp.hour)

    minutes = min_until_midnight()
    longest_s = gh_contributions.get_longest_streak("DrNotThatEvil")
    current_s = gh_contributions.get_current_streak("DrNotThatEvil")

    if gh_contributions.get_commited_today('DrNotThatEvil') == False:
        if timestamp.hour == 23:
            # Last hour of the day now lets remind the user every 15 minutes.
            if (timestamp.minute % 15) == 0 and timestamp.minute < 45:
                # fifteen minutes but not the last 45 minutes 
                text = "You only have {} minutes left to maintain your GitHub.com streak\n"
                text = text + "Your current streak is {} days.\nYour Longest streak is {} days"
                text = text.format(current_s, longest_s)
                send_reminder("Github streak Reminder", text, 1)

            if (timestamp.minute > 50):
                text = "IMPORTANT: You only have {} minutes! left to maintain your GitHub.com streak\n"
                text = text + "Your current streak is {} days.\nYour Longest streak is {} days"
                text = text.format(minutes, current_s, longest_s)
                send_reminder("Github streak Reminder", text, 1)
        else:
            text = "You have {} minutes left to commit something or you lose your GitHub.com streak.\n\n" 
            text = text + "Your current streak is: {} days.\nYour longest is {} days."
            text = text.format(minutes, current_s, longest_s)

            send_reminder("Github streak Reminder", text, 1)
    else:
        commited_today = True
        text = "You have commited today! Here are your stats.\n\n" 
        text = text + "Today's commit count: {}\n"
        commit_count, _ = gh_contributions.get_count_date('DrNotThatEvil')
        if longest_s == current_s:
            text = text + "You are currently on your longest commit streak!\n"
            text = text + "Your new record is: {}"
            text = text.format(commit_count, current_s)
        else:
            text = text + "Your current streak is: {} days.\nYour longest is {} days."
            text = text.format(commit_count, current_s, longest_s)
        send_reminder("Github streak Reminder", text, 1)

        
    t = threading.Timer(60, CheckContibutions)
    t.start()

if __name__ == "__main__":
    ##t = threading.Timer(1, CheckContibutions)
    ##t.start()
    CheckContibutions()
