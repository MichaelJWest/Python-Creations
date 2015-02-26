def error():
	print "Please try again"

def competent():
	print "So you're competent, well done!"
	exit(0)

def incompetent():
	print "So no... you are not meant to be a programmer."
	exit(0)
	
def congrats():
	print "Sweet! Level up with Tech Boss"
	exit(0)

def question_1():
	print "Are you currently a programmer? Y/N?"
	
	while True:
		answer_1 = raw_input("> ")
		if answer_1 == "Y":
			competent()
		elif answer_1 == "N":
			question_2()
		else:
			error()
			
def question_2():
	print "Have you ever been employed as a programmer? Y/N?"	
	
	while True:
		answer_2 = raw_input("> ")
		if answer_2 == "Y":
			competent()
		elif answer_2 == "N":
			question_3()
		else:
			error()
			
			
			
def question_3():
	print "Have you completed a college degree for CS or EE? Y/N?"
	
	while True:
		answer_3 = raw_input("> ")
		if answer_3 == "Y" or "N":
			question_4()
		else:
			error()
			
			
def question_4():
	print "Do you know how to code? Y/N?"
	
	while True:
		answer_4 = raw_input("> ")
		if answer_4 == "Y":
			question_5()
		elif answer_4 == "N":
			question_7()
		else:
			error()
			
					

def question_5():
	print "CS knowledge too? Y/N?"
	
	while True:
		answer_5 = raw_input("> ")
		if answer_5 == "Y":
			question_6()
		elif answer_5 == "N":
			question_7()
		else:
			error()
			
			
def question_6():
	print "Are there jobs requiring a skill set closely to yours? Y/N?"
	
	while True:
		answer_6 = raw_input("> ")
		if answer_6 == "Y":
			question_8()
		else:
			print """
			Keep in mind that job postings usually
			have a \"super set\" of the skills you
			need. Don't pass up applying if you don't 
			hit every bullet point! 
			"""
			question_7()

def question_7():
	print "Are you willing to learn new skills? Y/N?"
	
	while True:
		answer_7 = raw_input("> ")
		if answer_7 == "Y":
			congrats()
		elif answer_7 == "N":
			incompetent()
		else:
			error()
			

def question_8():
	print "Are there jobs nearby? Y/N?"
	
	while True:
		answer_8 = raw_input("> ")
		if answer_8 == "Y":
			competent()
		elif answer_8 == "N":
			question_9()
		else:
			error()

			
def question_9():
	print "Are you able to move for work? Y/N?"
	
	while True:
		answer_9 = raw_input("> ")
		if answer_9 == "Y":
			competent()
		elif answer_9 == "N":
			question_10()
		else:
			error()

def question_10():
	print "Can you freelance or run a product business? Y/N?"
	
	while True:
		answer_10 = raw_input("> ")
		if answer_10 == "Y":
			competent()
		elif answer_10 == "N":
			incompetent()
		else:
			error()
			
question_1()

			
