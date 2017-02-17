#Equal substrings, n <= 200
#abcabcabc
import time

# Input: length, string
# Output: boolean
def testString(L, s):
	#print "testString:\nL: %d" %(L)

	for i in range(1,len(s)/L):

		#print "testString:\ni: %d\ns1: %s\ns2: %s" %(i, s[0:L], s[L*i:L*(i+1)])

		if not(s[0:L] == s[L*i:L*(i+1)]):
			#print "testString: Failed!"
			return False

	return True

#Input: length
#Output: list of factors
def getFactors(L):
	f = []

	for i in range(1,(L/2) + 1):
		if L % i == 0:
			f += [i]
			#print "getFactors:\ni: %d, L: %d" %(i, L)

	return f

# Input: string
# Output: Max equal parts
def answer(s):
	factors = []

	#print "answer:\ns: %s, len: %d" %(s,len(s))

	factors = getFactors(len(s))

	#print "answer:\nfactors: %s" %(factors)

	if len(s) == 1:
		return len(s)

	if factors:
		for j in factors:
			for i in range(len(s)):
				s1 = s[i:] + s[:i]

				if testString(j, s1):
					return len(s1)/j

		return 1
	else:
		return 1

def test():
	if not(answer("abcabcabc") == 3):
		print "Test failed: abcabcabc"
	if not(answer("abcabc") == 2):
		print "Test failed: abcabc"
	if not(answer("abcabcabcg") == 1):
		print "Test failed: abcabcabcg"
	if not(answer("athannathann") == 2):
		print "Test failed: athannathann"
	if not(answer("aaaa") == 4):
		print "Test failed: aaaa"
	if not(answer("a") == 1):
		print "Test failed: a"
	if not(answer("kalsdfklawsfedkbnasklfbasklbdfaklshdfkljbaskdfaksjdbfkhjasfhkbahje") == 1):
		print "Test failed: kalsdfklawsfedkbnasklfbasklbdfaklshdfkljbaskdfaksjdbfkhjasfhkbahje"
	if not(answer("asdfasdfasdfasdfasdfasdfasdfasdfasdf") == 9):
		print "Test failed: asdfasdfasdfasdfasdfasdfasdfasdfasdf"
	if not(answer("ab") == 1):
		print "Test failed: ab"
	if not(answer("abcabcabc") == 3):
		print "Test failed: abcabcabc"
	if not(answer("abcabc") == 2):
		print "Test failed: abcabc"
	if not(answer("abcabcabcg") == 1):
		print "Test failed: abcabcabcg"
	if not(answer("athannathann") == 2):
		print "Test failed: athannathann"
	if not(answer("aaaa") == 4):
		print "Test failed: aaaa"
	if not(answer("a") == 1):
		print "Test failed: a"
	if not(answer("kalsdfklawsfedkbnasklfbasklbdfaklshdfkljbaskdfaksjdbfkhjasfhkbahje") == 1):
		print "Test failed: kalsdfklawsfedkbnasklfbasklbdfaklshdfkljbaskdfaksjdbfkhjasfhkbahje"
	if not(answer("asdfasdfasdfasdfasdfasdfasdfasdfasdf") == 9):
		print "Test failed: asdfasdfasdfasdfasdfasdfasdfasdfasdf"
	if not(answer("ab") == 1):
		print "Test failed: ab"
	if not(answer("abcabcabc") == 3):
		print "Test failed: abcabcabc"
	if not(answer("abcabc") == 2):
		print "Test failed: abcabc"
	if not(answer("abcabcabcg") == 1):
		print "Test failed: abcabcabcg"
	if not(answer("athannathann") == 2):
		print "Test failed: athannathann"
	if not(answer("aaaa") == 4):
		print "Test failed: aaaa"
	if not(answer("a") == 1):
		print "Test failed: a"
	if not(answer("kalsdfklawsfedkbnasklfbasklbdfaklshdfkljbaskdfaksjdbfkhjasfhkbahje") == 1):
		print "Test failed: kalsdfklawsfedkbnasklfbasklbdfaklshdfkljbaskdfaksjdbfkhjasfhkbahje"
	if not(answer("asdfasdfasdfasdfasdfasdfasdfasdfasdf") == 9):
		print "Test failed: asdfasdfasdfasdfasdfasdfasdfasdfasdf"
	if not(answer("ab") == 1):
		print "Test failed: ab"
	if not(answer("abcabcabc") == 3):
		print "Test failed: abcabcabc"
	if not(answer("abcabc") == 2):
		print "Test failed: abcabc"
	if not(answer("abcabcabcg") == 1):
		print "Test failed: abcabcabcg"
	if not(answer("athannathann") == 2):
		print "Test failed: athannathann"
	if not(answer("aaaa") == 4):
		print "Test failed: aaaa"
	if not(answer("a") == 1):
		print "Test failed: a"
	if not(answer("kalsdfklawsfedkbnasklfbasklbdfaklshdfkljbaskdfaksjdbfkhjasfhkbahje") == 1):
		print "Test failed: kalsdfklawsfedkbnasklfbasklbdfaklshdfkljbaskdfaksjdbfkhjasfhkbahje"
	if not(answer("asdfasdfasdfasdfasdfasdfasdfasdfasdf") == 9):
		print "Test failed: asdfasdfasdfasdfasdfasdfasdfasdfasdf"
	if not(answer("ab") == 1):
		print "Test failed: ab"

#s = str(raw_input())

#print "The answer is: %d slices" %(answer(s))
start_time = time.time()

test()
print("--- %s seconds ---" % (time.time() - start_time))
