# K-sum calculator

# Contributors:
#   Ray Campbell
#   Ryan Cheng
#   Nathan Cobb
#   Can Dalgir
#   Eric Kim

import itertools

# Number of test cases
T = int(raw_input())

# Main loop
for i in range(0,T):
    # Get N and K, integerize them
    N_Raw,K_Raw = raw_input().split()
    N = int(N_Raw)
    K = int(K_Raw)

    # Get the Ksums, integerize and sort them
    Ksums_Raw = raw_input().split()
    Ksums = [int(a) for a in Ksums_Raw]
    Ksums = sorted(Ksums)

    # Generate the dictionary of Ksums occurrences (counts)
    Occurrences = {}
    for i in Ksums:
        if i in Occurrences:
            Occurrences[i] += 1
        else:
            Occurrences[i] = 1

    # Set of guesses, use first element of Ksums to find first number
    Guesses = []
    Guesses += [Ksums[0] / K]

    # Set of guesses Ksums, add first element of Ksums
    GKsums = []
    GKsums += [Ksums[0]]

    # Make guesses until we guess the set of N numbers
    while len(Guesses) != N:
        # Generate subsets for Ksums calculations
        Guesses_Subsets = list(itertools.combinations_with_replacement(Guesses,K))
        GKsums = [] # Initialize

        # Calculate guesses Ksums
        for i in Guesses_Subsets:
            GKsums += [sum(i)]

        # Generate dictionary of guesses Ksums occurrences (counts)
        GOccurrences = {}
        for i in GKsums:
            if i in GOccurrences:
                GOccurrences[i] += 1
            else:
                GOccurrences[i] = 1

        # Use the first sorted Ksum that hasn't been guessed to find the next guess, then break so no more guesses are added
        for i in sorted(Occurrences):
            if i in GOccurrences:
                if Occurrences[i] != GOccurrences[i]:
                    # Subtract lowest guess to find next guess
                    # e.g. A+A+A+Guess = Lowest_Ksum, Guess = Lowest_Ksum - (A+A+A)
                    Guesses += [i-(Guesses[0]*(K-1))]
                    break
            else:
                Guesses += [i-(Guesses[0]*(K-1))]
                break

    # Print our guesses
    for i in Guesses:
        print i,
    print ""