# Write a function, which when iven one string (s) and two characters
# (c1 and c2), computes all pairings of contiguous ranges of c1s
# and c2s that have the same length.  Your function should return
# a set of three-tuples.  Each element of the set should be
# (c1 start index, c2 start index, length)
#
# Note that s may contain other characters besides c1 and c2.
# Example:
#  s = abcabbaacabaabbbb
#      01234567890111111  <- indices for ease of looking
#                1123456
#  c1 = a
#  c2 = b
#  Observe that there are the following contiguous ranges of 'a's (c1)
#  Length 1: starting at 0, 3, 9
#  Length 2: starting at 6, 11
#  And the following contiguous ranges of 'b's (c2)
#  Length 1: starting at 1, 10
#  Length 2: starting at 4
#  Length 4: starting at 13
#  So the answer would be
#  { (0, 1, 1), (0, 10, 1), (3, 1, 1), (3, 10, 1), (9, 1, 1), (9, 10, 1),
#    (6, 4, 2), (11, 4, 2)}
#  Note that the length 4 range of 'b's does not appear as there are no
#  Length 4 runs of 'a's.

import random
import time
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def matching_length_sub_strs(s, c1, c2):
    
    c1_ranges = defaultdict(list)
    c2_ranges = defaultdict(list)

    def find_ranges(char):
        ranges = defaultdict(list)
        i = 0
        n = len(s)
        while i < n:
            if s[i] == char:
                start = i
                while i < n and s[i] == char:
                    i += 1
                length = i - start
                ranges[length].append(start)
            else:
                i += 1
        return ranges
    
    c1_ranges = find_ranges(c1)
    c2_ranges = find_ranges(c2)

    # The set of matching tuples
    result = set()

    # For each length that exists in both c1 and c2 ranges
    for length in c1_ranges:
        if length in c2_ranges:
            # Create all possible combinations of starting indices
            c1_starts = c1_ranges[length]
            c2_starts = c2_ranges[length]
            # Use list comprehension for faster execution
            result.update({(c1_start, c2_start, length) for c1_start in c1_starts for c2_start in c2_starts})

    return result

# The string is mostly comprised of 'a' and 'b'
def rndstr(n):
    def rndchr():
        x = random.randrange(7)
        if x == 0:
            return chr(random.randrange(26) + ord('A'))
        if x <= 3:
            return 'a'
        return 'b'
    ans = [rndchr() for _ in range(n)]
    return "".join(ans)

# Best case: string without c1 and c2
def best(n):
    return 'x' * n  # 'x' is neither 'a' nor 'b'

# Worst case: alternating c1 and c2
def worst(n):
    s = ''
    c = 'a'  # Assuming c1 = 'a' and c2 = 'b'
    for _ in range(n):
        s += c
        c = 'b' if c == 'a' else 'a'
    return s


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)

    c1 = 'a'
    c2 = 'b'

    strgens = [("Best Case", best), ("Worst Case", worst), ("Random Input", rndstr)]
    Ns = [512 * 2**i for i in range(6)]  # Ns from 512 to 16,384

    print("N,Case,Time_ms")
    for N in Ns:
        for case_name, sg in strgens:
            s = sg(N)
            start_time = time.perf_counter()
            result = matching_length_sub_strs(s, c1, c2)
            end_time = time.perf_counter()
            elapsed_time_ms = (end_time - start_time) * 1000  # Convert to ms
            print(f"{N},{case_name},{elapsed_time_ms:.3f}")
            
            if elapsed_time_ms > 60000:  # 60 seconds
                print(f"Stopping at N={N} for {case_name} due to long runtime.")
                break  # Stop testing larger N for this case


Ns = np.array([512, 1024, 2048, 4096, 8192, 16384])
best_case_times = np.array([0.051, 0.209, 0.773, 3.292, 17.775, 74.511])
worst_case_times = np.array([7.216, 34.161, 143.085, 757.593, 4126.838, 790339.969])
random_input_times = np.array([2.209, 14.929, 57.414, 244.013, 1338.515])

# Adjust Ns and times for Random Input to match in length
Ns_random = Ns[:-1]  # Exclude the last N since we don't have data for it
random_input_times = random_input_times

plt.figure(figsize=(10, 6))

# Best Case
plt.plot(Ns, best_case_times, 'o-', color='green', label='Best Case')

# Worst Case
plt.plot(Ns, worst_case_times, 'o-', color='red', label='Worst Case')

# Random Input
plt.plot(Ns_random, random_input_times, 'o-', color='blue', label='Random Input')

# For O(N)
theoretical_O_N = best_case_times[0] * (Ns / Ns[0])
plt.plot(Ns, theoretical_O_N, '--', color='darkgreen', label='O(N) (Theoretical)')

# For O(N^2)
theoretical_O_N2 = worst_case_times[0] * (Ns / Ns[0])**2
plt.plot(Ns, theoretical_O_N2, '--', color='darkred', label='O(N^2) (Theoretical)')

# Set scales to logarithmic for better visualization
plt.xscale('log', base=2)
plt.yscale('log')


plt.xlabel('Input Size N')
plt.ylabel('Runtime (ms)')
plt.title('Runtime vs. Input Size for Different Cases')

plt.legend()

plt.show()

