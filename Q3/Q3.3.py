# Queue To Do
# ===========
#
# You're almost ready to make your move to destroy the LAMBCHOP doomsday device, but the security checkpoints that guard the underlying systems of the LAMBCHOP are going to be a problem. You were able to take one down without tripping any alarms, which is great! Except that as Commander Lambda's assistant, you've learned that the checkpoints are about to come under automated review, which means that your sabotage will be discovered and your cover blown - unless you can trick the automated review system.
#
# To trick the system, you'll need to write a program to return the same security checksum that the guards would have after they would have checked all the workers through. Fortunately, Commander Lambda's desire for efficiency won't allow for hours-long lines, so the checkpoint guards have found ways to quicken the pass-through rate. Instead of checking each and every worker coming through, the guards instead go over everyone in line while noting their security IDs, then allow the line to fill back up. Once they've done that they go over the line again, this time leaving off the last worker. They continue doing this, leaving off one more worker from the line each time but recording the security IDs of those they do check, until they skip the entire line, at which point they XOR the IDs of all the workers they noted into a checksum and then take off for lunch. Fortunately, the workers' orderly nature causes them to always line up in numerical order without any gaps.
#
# For example, if the first worker in line has ID 0 and the security checkpoint line holds three workers, the process would look like this:
# 0 1 2 /
# 3 4 / 5
# 6 / 7 8
# where the guards' XOR (^) checksum is 0^1^2^3^4^6 == 2.
#
# Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process would look like:
# 17 18 19 20 /
# 21 22 23 / 24
# 25 26 / 27 28
# 29 / 30 31 32
# which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.
#
# All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and the checkpoint line will always be at least 1 worker long.
#
# With this information, write a function answer(start, length) that will cover for the missing security checkpoint by outputting the same checksum the guards would normally submit before lunch. You have just enough time to find out the ID of the first worker to be checked (start) and the length of the line (length) before the automatic review occurs, so your program must generate the proper checksum with just those two values.
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
#
# Test cases
# ==========
#
# Inputs:
#     (int) start = 0
#     (int) length = 3
# Output:
#     (int) 2
#
# Inputs:
#     (int) start = 17
#     (int) length = 4
# Output:
#     (int) 14
def answer(start, length):
    ans = 0
    #calculate xor for every row, and xor it with the final answer
    for x, y in enumerate(reversed(range(1, length+1))):
        ans = ans ^ helper(start+x*length, y)
    return ans

#calculates xor given a row (such as 20 to 25, or 25 to 29 given start = 20 and length = 5)
#because each row is guaranteed to increment by 1 for the duration of length,
#we can use this fact to calculate the xor for the row without needing to actually xor the rest.
#There is a pattern for each digit in binary. For example for the 1's place alternates
#0101 as you increment by 1, and the 2's place follows the pattern 00110011.
def helper(start,length):
    twos = 2
    temp = True
    xored = ''
    while temp:
        #This tells us where in the pattern we are starting
        start_remainder = start % twos
        #this is the position in the pattern which we should finish at after length amount of numbers
        #the key is that as we go through length, we are always incrementing by 1
        position = start_remainder + (length % twos)
        # the 1's place is different than the rest because finishing the pattern
        # doesn't mean it resets at 0, while for others, finishing a pattern means the xor is 0
        # because they have an even amount of 1's in the pattern.
        if twos == 2:
            #this array is the pattern of xor'ed bits will take
            array = [0,1,1,0]
            xored += str(array[(start_remainder%4+length-1)%4])
            twos *= 2
            continue
        #in this case, the position goes past the end of the pattern.
        #if the position is before where the 1's start to appear, then
        #we can treat it as if it just finished the pattern.
        #it can also cycle past the pattern multiple times, but that doesn't matter
        if position % twos < twos/2:
            position = twos

        if start_remainder < (twos/2):
            #in this case, we start in the 0's but end up in the 1's somewhere
            #if we have an odd offset into the group of 1's, then
            #the xor is a 1. Otherwise, the xor of this digit is a 0.
            if (position - twos/2)%2 == 1:
                xored += str(1)
            else:
                xored += str(0)
        else:
            #in this case, we started within the group of 1's and the position
            #is a little farther within the 1's. Again, if we have an odd offset
            #into the 1's then the xor is a 1.
            if (position - start_remainder) % 2 == 1:
                xored += str(1)
            else:
                xored += str(0)
        #stop calculating extra digits
        if (start+length-1) / twos < 1:
            temp = False
        twos *= 2
    #return the int representation of the reverse xored
    #because we are appending using strings, we need to reverse.
    return int(xored[::-1],2)
def main():
    print(answer(150,50))
    print(checker(150,50))

    # ans = 0
    # for x in range (250,265):
    #     ans = ans ^ x
    # print(ans)
    # print(helper(250,15))

    # ans = 0
    # for x in range(9, 20):
    #     ans = ans ^ x
    # print(ans)
    # print(helper(9,11))

def checker(start,length):
    ans = 0
    # print('hi')
    for x, y in enumerate(reversed(range(1, length + 1))):
        # print(f'x is {x}')
        # print(f'y is {y}')
        row = 0
        # print(f'printing from {start+length*x} to {start+length*x+y}')
        for temp in range(start+length*x, start+length*x+y):
            # print(f'temp is {temp}')
            row = row ^ temp
        # print(f'row is {row}')
        # print(f'row in binary is {bin(row)}')
        ans = ans ^ row
            # print(ans)
    return ans

if __name__ == "__main__":
    main()