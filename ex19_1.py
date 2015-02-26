import datetime

def giving_up_timer(arg1, arg2, arg3):
	print "I have given up gaming for %r days" % (arg1.days)
	print "I have given up facebook for %r days" % (arg2.days)
	print "I have given up alcohol for %r days" % (arg3.days)
	print "Good job so far!"

date = datetime.date.today()
no_gaming_date = datetime.date(2015, 2, 20)
no_facebook_date = datetime.date(2015, 2, 18)
no_alcohol_date = datetime.date(2015, 2, 17)
giving_up_timer(date - no_gaming_date, date - no_facebook_date, date - no_alcohol_date)

	