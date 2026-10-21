# Program to display current date and time using datetime module

from datetime import datetime

now = datetime.now()

print("Current Date and Time:", now)
print("Current Date:", now.date())
print("Current Time:", now.time())
