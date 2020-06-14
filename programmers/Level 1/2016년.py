# https://programmers.co.kr/learn/courses/30/lessons/12901


import datetime

def solution(a, b):
    weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return weekday[datetime.datetime(2016, a, b).weekday()]
