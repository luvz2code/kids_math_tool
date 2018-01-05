#! /usr/bin/python

import random
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


MAX_NUMBER_OF_PROBLEMS = 25

name = raw_input("Enter your name : ")

print bcolors.HEADER + "Hello ", str(name) + bcolors.ENDC
print ""

results = []
total_time = 0

ctr = 0

correct = 0
wrong = 0

while ctr < MAX_NUMBER_OF_PROBLEMS:
	x = random.randint(1,12)
	y = random.randint(1,x)
	z = x / y

	while True:
		t0 = time.time()
		raw_ans = raw_input("What is " + str(x) + " / " + str(y) + " : ")
		t1 = time.time()
		total_time = t1-t0

		try:
			ans = int(raw_ans)
	
			if (ans == z):
				correct = correct+1
			else:
				wrong = wrong+1
				results.append("" + str(x) + " / " + str(y) + " : Your answer : " + str(ans) + " Correct answer : "+ str(z) + "")
		
			ctr = ctr+1
			break

		except ValueError:
			print bcolors.FAIL + "Invalid number. Try again." + bcolors.ENDC

print ""	
print "Done. Your answers.."

print "Time taken ", str(total_time)
print "Correct ", str(correct)
print "Wrong ", str(wrong)

print ""

for result in results:
	print bcolors.FAIL + result + bcolors.ENDC

print ""
print "Goodbye ", str(name)


 




