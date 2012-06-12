#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def is_leap_year(year):
	if (year % 400) == 0:
		return True
	elif (year % 100) == 0:
		return False
	elif (year % 4) == 0:
		return True
	else:
		return False

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


x = 1900
start = x + 1
end = 2000
days_in_x = sum(days_in_month)
if(is_leap_year(x)):
	days_in_x += 1

#When is the first Sunday in 1901?
#Since we know that Jan 1, 1900 was a Monday...
sunday_index = 5 #((days_in_x-1) % 7);

total_days = 0
sundays = 0
for year in range(start, end+1):
	for month in range (0, len(days_in_month)):
		print(year, month+1, days_in_month[month], is_leap_year(year), total_days, sundays)
		if (((total_days+1) % 7) == sunday_index):
			sundays += 1
		days = days_in_month[month]
		if ((month == 1) and is_leap_year(year)):
			days += 1
		total_days += days
		
print(sundays)
