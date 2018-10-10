# def answer(n):
#     checked_array = {}
#     counter = 0
#     not_checked_array = []
#     list_pairs(n,1, not_checked_array)
#     while(len(not_checked_array)!=0):
#         for combo in not_checked_array:
#             # print(f'combo is {combo}')
#             # checked_array.append(combo)
#             counter +=1
#             not_checked_array.remove(combo)
#             remainder_array = combo[0:len(combo) - 1]
#             temp_array=[]
#             list_pairs(combo[len(combo)-1], combo[len(combo)-2]+1, temp_array)
#             # print(f'temp array is {temp_array}')
#             if temp_array != []:
#                 for x in temp_array:
#                     new_combo = remainder_array + x
#                     not_checked_array.append(new_combo)
#     #         print(f'not_checked array is {not_checked_array}')
#     # print(f'checked array is {checked_array}')
#     return counter
# def list_pairs(num, start, array):
#     temp_array = []
#     if num%2 ==0:
#         temp = int(num/2)
#     else:
#         temp = int(num/2)+1
#     if start>=temp:
#         return False
#     for x in range(start, temp):
#        array.append([x,num-x])
#     return True
# def answer(n):
#     return recursive_pair(n,1)
# def recursive_pair(num,start):
#     counter = 0
#     if num % 2 == 0:
#         temp = int(num / 2)
#     else:
#         temp = int(num / 2) + 1
#     if start > temp:
#         return 0
#     for x in range(start, temp):
#        counter += recursive_pair(num-1, x+1)+1
#     return counter

#write a function that takes an integer n and returns number of staircases you can build
#from exactly n bricks. n is more than 3 but no more than 200
#staircase must be in ascending order, each step must have at least one brick
# n=5 has (1,4) and (2,3)
# n =6 has (1,5),(2,4), (1,2,3)

#I wish I could show a picture of what I wrote down.
#I found that for n number of bricks, it is dependent
#on the values found from the previous numbers of bricks.

#For example: for n=6, it becomes (1,5) and (2,4)
#and then we can expand on (1,5) by checking the values from
#n=5, which were (1,4) and (2,3). We notice that as we split up the 5,
#we can't use (1,1,4) because we already used 1, so we skip that and use (1,2,3)

#I originally tried to do it recursively but it took too long.
#Instead, I decided to build up values along iterations, which is much faster.
def answer(n):
    array = [0] * 201
    for temp in range(201):
        #only create the amount of spaces in array as necessary
        array[temp] =[0] * (int((temp+1)/2)+1)
    #there will be an extra 0 at slot 0 for all x and when x is 0-2 but it helped me visualize it better this way
    for x in range(3, n + 1):
        array[x][int((x-1)/2)]=1
        #the value at [x][y] is the sum of the values past the y'th row
        for y in range(1,int((x-1)/2)):
            array[x][y] = sum(array[x-y][y+1:])+1
    return sum(array[n])

def main():
    temp_array = [1,2,3,4,5]
    #print(recursive_pair(7,1))
    #print(list_pairs(7,2+1, temp_array))
    #print(temp_array)
    #print(answer(12))
    print(answer(200))

if __name__ == "__main__":
    main()