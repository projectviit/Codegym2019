
months = [ 'jan', 'feb','mar','apr','may','jun','jul','agu','sep','oct','nov','dec', ]

days = {
	
	'jan' : 31,
	'feb' : 31,
	'mar' : 31,
	'apr' : 30,
	'may' : 31,
	'jun' : 30,
	'jul' : 31,
	'agu' : 31,
	'sep' : 30,
	'oct' : 31,
	'nov' : 30,
	'dec' : 31,
}

sunday_count = 0

current_date = 6 # Sunday on 6th Jan 1901

for year in range(1901,2001):
	if year%4 == 0:                  #leap year
		days['feb'] = 29
	else:
		days['feb'] = 28

	for month in months :
		while current_date <= days[month]:
			current_date = current_date + 7
		current_date = current_date - days[month]
		if current_date == 1:
			sunday_count = sunday_count+1
			#print(f"date: {current_date}/{month}/{year}")


print(sunday_count)