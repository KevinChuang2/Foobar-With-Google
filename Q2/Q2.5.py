#given a list of digits, find the largest number you can make out of
#the digits that is divisible by 3.
#for example: {3,1,4,1} would return 4311 because it is divisible by 3
def answer(l):
    list_finished = []
    list1 = []
    list2 = []
    for num in l:
        #if the number is divisible by 3, it is always included in solution
        if num%3 == 0:
            list_finished.append(num)
        if num%3 == 1:
            list1.append(num)
        if num%3 == 2:
            list2.append(num)
    # list1 contains numbers who's remainder when divided by 3 is 1
    list1.sort(reverse=True)
    # list2 contains numbers who's remainder when divided by 3 is 2
    list2.sort(reverse=True)
    while len(list1) >= 3:
        # 3 numbers who have remainder of 1 can always be included
        # since it is sorted, we always just add the number at the front of the list
        # because it is the greatest number with remainder of 1
        for x in range(0,3):
            list_finished.append(list1[0])
            del list1[0]
    while len(list2) >= 3:
        # 3 numbers who have remainder of 2 can always be included
        for x in range(0, 3):
            list_finished.append(list2[0])
            del list2[0]
    # can never add numbers in this case
    if len(list2) == 0 or len(list1) == 0:
        pass
    # only case where we can add two of the %3==1 and %3=2
    elif len(list2) == 2:
        if len(list1) == 2:
            for x in range(0, 2):
                list_finished.append(list1[0])
                list_finished.append(list2[0])
    # otherwise, best we can do is one of the %3==1 and one of the %3==2
    else:
        list_finished.append(list1[0])
        list_finished.append(list2[0])
    list_finished.sort()
    temp = 1
    answer = 0
    for num in list_finished:
        answer += num*temp
        temp *= 10
    return answer


def main():
    list = [3,1,4,1]
    print(answer(list))

if __name__ == "__main__":
    main()