# jam_session_6-6-19.py - implements the problems associated with
# 						  the PyAtl Jam Session on 6/6/19.
#
#						problem: essentially, the object is to
#						implement the fizz buzz problem in 
#						several different ways.

from pprint import pprint

def problem1(n):
	''' type(n) -> int '''
	for i in range(1, n+1):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

def problem2(n):
	''' type(n) -> int '''
	ret_val = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0
				else "Fizz" if i % 5 == 0
				else "Buzz" if i % 3 == 0
				else i
				for i in range(1, n+1)
			  ]
	pprint(ret_val)

def problem3(n):
	''' type(n) -> int '''
	pass

def problem4(n):
	''' type(n) -> int '''
	if n == 0:
		return

	if n % 3 == 0 and n % 5 == 0:
		print("FizzBuzz")
		problem4(n-1)
	elif n % 3 == 0:
		print("Fizz")
		problem4(n-1)
	elif n % 5 == 0:
		print("Buzz")
		problem4(n-1)
	else:
		print(n)
		problem4(n-1)

def problem5_generator(n):
	''' type(n) -> int '''
	if n % 3 == 0 and n % 5 == 0:
		print("FizzBuzz")
	elif n % 3 == 0:
		print("Fizz")
	elif n % 5 == 0:
		print("Buzz")
	else:
		print(n)

	while n > 0:
		yield n
		n -= 1

def problem5_caller(n):
	''' type(n) -> int '''
	while n > 0:
		next(problem5_generator(n))
		n -= 1

def main():
	
	#############
	# PROBLEM 1 #
	#############

	# test_num1 = 100
	# problem1(test_num1)

	#############
	# PROBLEM 2 #
	#############

	# test_num2 = 100
	# print(problem2(test_num2))

	#############
	# PROBLEM 3 #
	#############

	#############
	# PROBLEM 4 #
	#############
	# test_num4 = 100
	# problem4(test_num4)

	#############
	# PROBLEM 5 #
	#############
	test_num5 = 100
	problem5_caller(test_num5)

if __name__ == "__main__":
	main()