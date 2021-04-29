import datetime
import time

#this code retrieves the date and time from the computer, to create the timestamp

for x in range(10):

    right_now = datetime.datetime.now().isoformat()
    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    tim = ("".join(list))

    print(tim)

    time.sleep(.001)

