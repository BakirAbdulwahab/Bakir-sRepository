
age = input("What is your current age? ")

yearsLeft = 90 - int(age)
daysLeft = 365 * yearsLeft
weeksLeft = 52 * yearsLeft
monthsLeft = 12 * yearsLeft

totalTime = f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left..."

print(totalTime)