# Nathan Cobb
# 10/14/2016
# Google Coding Challenge 1-1
import time

# Find the maximum number of identical substrings, without any remaining characters
# Input:  s (string)
# Output: Maximum number of identical substrings, without any remaining characters
def answer(s):
    # Dictionary of sequences
    sequences = {}

    # For entire string, from different starting points
    for i in range(len(s)):

        # Modify the string according to the starting point
        string = s[i:] + s[:i]

        # For substrings of all lengths
        for j in range(len(s) + 1):
            # Check if the entire cake would be used for the given substring
            if (string.count(string[:i]) * len(string[:i])) == len(string):
                sequences[string[:i]] = string.count(string[:i])

    # Return the answer
    if sequences:
        return sequences[max(sequences, key=sequences.get)]
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

# Main
if __name__ == "__main__":
    # Get the input
    #s = raw_input()

    # Call the function, if input is valid
    #if len(s) < 200:
    #    result = answer(s)

    # Print the result
    #print result
    #s = str(raw_input())

    #print "The answer is: %d slices" %(answer(s))
    start_time = time.time()

    test()
    print("--- %s seconds ---" % (time.time() - start_time))
    
