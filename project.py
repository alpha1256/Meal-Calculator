import datetime

#Meal and flex input
meals = int(input("Enter how many meals you have left: "))
flex= float(input("Enter how many flex you have left: "))

#Entering current date
date_entry = input('Enter the day the semester end in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)

#Getting current date
currentDate = datetime.datetime.today().strftime ('%Y-%m-%d')
year,month,day = map(int,currentDate.split('-'))
date2 = datetime.date(year,month,day)

#Getting current 
dayRemain = (date1 - date2).days
print("MEALS: ",meals, "\nFLEX:",flex, "\nDAYS REMAIN:",dayRemain)


mealAte = int(input("Enter how many meals you want to use out of your meal plan"))
flexPlan = int(input("Enter how many pandas you want to use during the day"))

choice = input("Do you want to have panda every other day 'y' or 'n'")

holidays = int(input("How many holidays do you have"))

dayRemain = dayRemain - holidays

counter = 1
while counter < dayRemain:
	form = counter % 2
	if choice == 'n' or choice =='y' and form == 0:
		meals = meals - mealAte
		flex = flex - (6.58 * flexPlan)
	elif choice == 'y' and form == 1:
		meals = meals - (mealAte + 1)   

	print("At the end of the day ",counter, " you have ", meals, " meals and flex ", flex )
	if meals == 0:
		print("At day ", counter, " you ran out of meals")
		break
	elif flex <= 0:
		print("At day", counter, " you ran out of flex points")
		break
	
	counter = counter + 1

print("You have flex ", flex, " and meals ", meals ,"remaining ")