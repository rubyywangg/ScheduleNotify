import menu
import notifiers
import schedule
import time as tm #creates a time
from datetime import time, timedelta, datetime #built-in python module (timedelta --> time difference)

def main():
    """Program execution starts here."""

    # Set up main menu and sub-menus.
    schedule_tasks = ["Add Task", "Schedule Task", "Edit Task"]
    time_menu_options = ["By seconds","Minutely", "Hourly", "Specific Time"]

    while True:
        choice = menu.do_menu("Choose a menu option:",
                              schedule_tasks)
        # Did the user choose "Exit?"
        if choice is None:
            # Yes, then exit.
            break
        if choice == 1:  # User chose temperature conversions.
            # Loop until user wants to return to the main menu.
                task_list=[]
                end = False
                while end != True:
                    task_item = str(input("Task: "))
                    if task_item not in ["end", "stop", "leave"]:
                        task_list.append(task_item)
                        print(task_list)
                    else:
                         end = True
        if choice == 2:  # User chose temperature conversions.
            # Loop until user wants to return to the main menu.
                for i in range (len(task_list)):
                     schedule_time = menu.do_menu("Schedule a time for each task:", time_menu_options)
                     if schedule_time == 1:
                          seconds = int(input("How many seconds apart fo you want to set the notifications? "))
                          notifiers.by_seconds(seconds, task_item[i])


   
if __name__ == "__main__":
    main()
# def user_tasks():
#     while True:
#         task = str(input("Enter a task: "))



# def job():
#     print("New tasks")

# def daily_reminder():
#     print("drink water")


# schedule.every(5).seconds.do(job) #scheduling task every 5 seconds to do job
# schedule.every().day.at("13:03").do(daily_reminder)
# schedule.every().minute.at(":40").do(job) #do the job eery minute at 40 seconds
# # schedule.every().hour.until(time(11,33,42)).do(job) #dp every hour until you reached 11 hours, 33 minutes and 42 seconds
# # schedule.every().hour.until(timedelta(hours=8)).do(job) #run this all the time for 8 hours
# # j = schedule.every(1).to(5).seconds.do(job) #generate random intervals between 1 and 5 and run this

# # counter = 0

# while True:
#     schedule.run_pending() #applies the schedule
#     tm.sleep(1) #delay for 1 second
#     counter +=1
#     # if counter==10:
#     #     schedule.cancel_job(j)
