import datetime

now = datetime.datetime.now()
print("The current date and time is:", now)

with open("data.txt", "w") as f:
    f.write("This file was generated on " + str(now) + "\n")
