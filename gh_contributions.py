#!/usr/bin/env python
#
# Print your contributions for the current day
# Usage: ghb contributions
#

import signal
import sys
from datetime import datetime
from html.parser import HTMLParser
from requests import get

URL = "https://github.com/users/%s/contributions"

class CustomHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rects = []

    def handle_starttag(self, tag, attrs):
        if tag == "rect":
            self.rects.append(attrs)


def signal_handle(sig, frame):
    sys.exit(0)


def pluralize(number):
    if number == 1:
        return ""
    return "s"

def get_count_date(username):
    r = get(URL % username)
    parser = CustomHTMLParser()
    parser.feed(r.text)
    d = dict(parser.rects[-1])
    number = d["data-count"]
    date = d["data-date"]
    return number, date

def get_current_streak(username):
    r = get(URL % username)
    parser = CustomHTMLParser()
    parser.feed(r.text)
    
    rev_rects = list(reversed(parser.rects))
    d_now = dict(rev_rects[0])
    if int(d_now["data-count"]) == 0:
        rev_rects.pop(0)

    count = 0
    for i in rev_rects:
        d = dict(i)
        if int(d["data-count"]) > 0:
            count = count + 1
        else:
            break

    return count

def get_longest_steak(username):
    r = get(URL % username)
    parser = CustomHTMLParser()
    parser.feed(r.text)

    max_steak = 0
    count = 0 
    for i in reversed(parser.rects):
        d = dict(i)
        if int(d["data-count"]) > 0:
            count = count + 1
        else:
            if count > max_steak:
                max_streak = count
                count = 0
    
    return max_streak

def get_commited_today(username):
    num, date = get_count_date(username)
    num = int(num)
    cur_date = datetime.now().strftime('%Y-%m-%d')
    if date == cur_date:
        if num > 0:
            return True
    return False
