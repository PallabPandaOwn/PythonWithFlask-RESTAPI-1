# Age convertor
input_age = int(input("Please enter your age : "))
total_Months = input_age * 12
hoursInMonths = 24 * 30  # Hours in month
secondsInDay = 24 * 60 * 60  # Seconds in month
# print(secondsInDay)
print("your age {} is equivalent to {} months ,{} hours and {} seconds.".format(input_age, total_Months, hoursInMonths,
                                                                                secondsInDay))
