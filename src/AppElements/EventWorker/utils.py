import datetime
import time

def getConstructedTimeFormat(day, month, time): 
    return day + ' ' + month + " о " +  time

def getcurrentTimestamp():
    return int(time.time())

def getFullDateTimestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

def getTimeFromTimestamp(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).strftime('%H:%M')