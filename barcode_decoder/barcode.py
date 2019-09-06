# barcode.py - this prgm will attempt to solve the problems associated with
#			   9/5 python jam session.
#
# jack f - 9/5

#################
### PROBLEM 1 ###
#################

# decode the left digits
def problem1(bstring):
	'''
	input:
		bstring -> Str
	output:
		Int (or Boolean)
	'''

	# setup map
	map = {
		"0001101":	0,
		"0011001":	1,
		"0010011":	2,
		"0111101":	3,
		"0100011":	4,
		"0110001":	5,
		"0101111":	6,
		"0111011":	7,
		"0110111":	8,
		"0001011":	9
	}

	# check if binary string is in map
	for v in map:
		if v == bstring:
			return map[v]

	# else none
	return None

def test_decode_left():
	tests = [
		("0001101", 0),
		("0111011", 7),
		("0011001", 1),
		("0000000", None)
	  ]

	for test in tests:
		print("\n=========================")
		print("Testing:", test)
		print("calling: problem1(" + test[0] + ")")
		print("answer:", test[1])
		print("correct ?", problem1(test[0]) == test[1])

#################
### PROBLEM 2 ###
#################

# decode left and right codes
def problem2(bstring):
	'''
	input:
		bstring -> Str
	output:
		Int (or Boolean)
	'''

	# setup map
	l_map = {
		"0001101":	0,
		"0011001":	1,
		"0010011":	2,
		"0111101":	3,
		"0100011":	4,
		"0110001":	5,
		"0101111":	6,
		"0111011":	7,
		"0110111":	8,
		"0001011":	9
	}

	r_map = {}
	for key, val in l_map.items():
		new_str = ''
		for char in key:
			if char == '0':
				new_str += '1'
			else:
				new_str += '0'
		r_map[new_str] = val

	# check if binary string is in l_map
	for val in l_map:
		if val == bstring:
			return l_map[val]
	# check in r_map
	for val in r_map:
		if val == bstring:
			return r_map[val]

	# else none
	return None

def test_problem_2():
	tests = [
		("1110010", 0),
		("1000100", 7),
		("1100110", 1)
	]

	for test in tests:
		print("\n=========================")
		print("Testing:", test)
		print("calling: problem2(" + test[0] + ")")
		print("answer:", test[1])
		print("correct ?", problem2(test[0]) == test[1])

#################
### PROBLEM 3 ###
#################

# decode barcode given the block string
def problem3(bstring):
	'''
	input:
		bstring -> Str
	output:
		digits -> Str
	'''

	# redefine problem2
	get_digit = problem2

	# check that beginning & ending are valid '101'
	if bstring[0:3] != '101':
		return None
	if bstring[-3:] != '101':
		return None

	left_half = bstring[3:45]
	# print("left_half:", left_half)
	right_half = bstring[50:len(bstring)-3]
	# print("right_half:", right_half)

	digits = ''
	# check left half first
	for i in range(6):
		block = left_half[7*i:7*(i+1)]
		print("current left_block:", block)
		digits += str(get_digit(block))
	# check right half second
	for i in range(6):
		block = right_half[7*i:7*(i+1)]
		print("current right_block:", block)
		digits += str(get_digit(block))
	
	return digits

def test_problem_3():
	tests = [
		(
		"075755331853",
		"10100011010111011011000101110110110001011000101010100001010000101100110100100010011101000010101"
		),
		(
		"760712090019",
		"10101110110101111000110101110110011001001001101010111001011101001110010111001011001101110100101"
		),
		(
		"037431882400",
		"10100011010111101011101101000110111101001100101010100100010010001101100101110011100101110010101"
		),
		(
		"296480306484",
		"10100100110001011010111101000110110111000110101010100001011100101010000101110010010001011100101"
		),
		(
		"193872293318",
		"10100110010001011011110101101110111011001001101010110110011101001000010100001011001101001000101"
		)
	]

	for test in tests:
		print("\n=========================")
		print("Testing:", test)
		print("calling: problem3(" + test[1] + ")")
		print("answer:", test[0])
		print("correct ?", problem3(test[1]) == test[0])

###############
### TESTING ###
###############

def main():
	# test problem 1
	# test_decode_left()

	# test problem 2
	# test_problem_2()

	# test problem 3
	test_problem_3()

if __name__ == "__main__":
	main()