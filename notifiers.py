import schedule
import time as tm #creates a time
from datetime import time, timedelta, datetime #built-in python module (timedelta --> time difference)

def by_seconds(seconds, task_item):
    schedule.every(seconds).seconds.do(task_item)

def main():
    seconds = int(input("How many seconds apart fo you want to set the notifications? "))
    by_seconds(seconds, "yes")

if __name__=="__main__":
    main()