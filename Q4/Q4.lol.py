import math
def answer(times, time_limit):

    answer = []
    #print('Times original:')
    # for x in range(0, len(times)):
    #     print(times[x])
    shortest_graph = []
    # print('Graph after bford:')
    lengths = bford(0, times)
    # print(lengths)
    #check for negative cycles
    if lengths == 'Negative Cycle':
        #return all bunnies because if there's a neg cycle, we can get to any bunny
        for i in range(0, len(times)-2):
            answer.append(i)
        return answer
    #construct graph of shortest paths using bford on each vertice. This speeds
    #up the search
    for x in range(0, len(times)):
        lengths = bford(x, times)
        print(lengths)
        shortest_graph.append(lengths)
    times = shortest_graph
    smallest_nums = [None]*len(times[0])
    smallest = times[0][0]
    for x in range(0,len(times[0])):
        smallest_nums[x] = [float('inf'), x]
    for temp, x in enumerate(times):
        for count, y in enumerate(x):
            if y < smallest:
                smallest = y
            if times[temp][count] < smallest_nums[count][0] and temp != count and count !=0:
                smallest_nums[count][0] = times[temp][count]
    time_limit = time_limit-smallest_nums[len(times[0])-1][0]
    smallest_nums = smallest_nums[1:-1]

    # print(time_limit)
    while sum(x[0] for x in smallest_nums) > time_limit:
        if smallest_nums:
            smallest_nums.reverse()
            temp_max = max(x[0] for x in smallest_nums)
            for x in smallest_nums:
                # print(temp_max)
                if x[0] == temp_max:
                    smallest_nums.remove(x)
                    break
            smallest_nums.reverse()
        else:
            return []
        # print(smallest_nums)
        # print(sum(x[1] for x in smallest_nums))
        # smallest_nums.remove(max(x[0] for x in smallest_nums))
    print(smallest_nums)
    print(time_limit)
    possible_list = [x[1] for x in smallest_nums]

    # queue = []
    # for x in range(1,len(times)):
    #     queue.append([[0,x], time_limit-times[0][x]])
    # queue.sort(key=lambda x:x[1], reverse=True)
    # print(f'queue is {queue}')
    # finished = []
    # counter = 0
    # #print(queue)
    #
    # while queue:
    #     print(f'queue is {queue}')
    #     #print(f'finished is {finished}')
    #     # print(f'queue len is {len(queue)}')
    #     counter+=1
    #     print(f'counter is {counter}')
    #     last_node = queue[0][0][-1]
    #     last_time = queue[0][1]
    #     #print(f'last node is {last_node}')
    #     added_move = queue[0]
    #     # print(f'added move is {added_move}')
    #     # print(f'count is {added_move[0].count(x)}')
    #     if last_node == len(times)-1:
    #         if added_move[1]>=0:
    #             finished.append(added_move)
    #             if len(set(added_move[0])) == len(times):
    #                 break
    #     for x in range(0, len(times)):
    #         if x == last_node:
    #             pass
    #         elif added_move[0].count(x)>len(times)-1:
    #             break
    #         else:
    #             #print(f'added move is {added_move}')
    #             temp = [[],0]
    #             for i in added_move[0]:
    #                 temp[0].append(i)
    #             temp[0].append(x)
    #             temp[1]=last_time - times[last_node][x]
    #             if temp[1] < smallest:
    #                 continue
    #             else:
    #                 # if queue:
    #                 #     if len(set(queue[0][0]))<len(set(temp[0])):
    #                 #         queue.insert(1,temp)
    #                 #     else:
    #                 #         queue.append(temp)
    #                 if len(temp[0]) > 2:
    #                     # print(f'temp is {temp}')
    #                     last_occurence = len(temp[0][::-1][1:]) - 1 - temp[0][::-1][1:].index(x) if x in temp[0][::-1][1:] else -1
    #                     # print(f'last occ: {last_occurence}')
    #                     # print(f'x is {x}')
    #                     if last_occurence == -1:
    #                         # print(f'inserted {temp} early')
    #                         queue.insert(1,temp)
    #                         continue
    #                     elif last_occurence == 0:
    #                         queue.append(temp)
    #                     if temp[0][-2] != temp[0][last_occurence-1]:
    #                         queue.append(temp)
    #     del(queue[0])
    #
    # finished.sort(key=lambda x:len(set(x[0])), reverse=True)
    # #print(finished)
    # if finished:
    #     max = len(set(finished[0][0]))
    # else:
    #     return []
    # print(finished)
    # best_moves = []
    # best_times = []
    # for move in finished:
    #     if len(set(move[0])) == max:
    #         set_temp = set(move[0])
    #         set_temp.remove(0)
    #         set_temp.remove(len(times)-1)
    #         best_moves.append(set_temp)
    #         best_times.append(move[1])
    # best_moves.sort(key=lambda x:sum(x))
    # list_of_bunnies = list(best_moves[0])
    # for x in range(0,len(list_of_bunnies)):
    #     list_of_bunnies[x] -= 1
    # return list_of_bunnies

def bford(source, graph):
    distance = []
    #pred = []
    for x in range(0,len(graph)):
        distance.append(float('inf'))
        #pred.append(0)
    distance[source] = 0
    #print(source)
    #print(graph)
    #print(f'distance is {distance}')
    #print(f'pred is {pred}')
    for i in range(0, len(graph)-1):
        for vertex_num, vertex in enumerate(graph):
            for target, edge in enumerate(vertex):
                if distance[vertex_num] + graph[vertex_num][target] < distance[target]:
                    distance[target] = distance[vertex_num] + graph[vertex_num][target]
                    #pred[target] = vertex_num
    #print(f'distance is {distance}')
    #print(f'pred is {pred}')
    for vertex_num, vertex in enumerate(graph):
        for target, edge in enumerate(vertex):
            if distance[vertex_num] + graph[vertex_num][target] < distance[target]:
                return 'Negative Cycle'
    return distance

def main():
    # graph = [
    #     [0, 2, 2, 2, 2, 2, 2],  # 0 = Start
    #     [2, 2, 2, 2, 2, 2, 2],  # 1 = Bunny 0
    #     [2, 2, 2, 2, 2, 2, 2],  # 2 = Bunny 1
    #     [2, 2, 2, 2, 2, 2, 2],  # 3 = Bunny 2
    #     [2, 2, 2, 2, 2, 2, 2],  # 4 = Bunny 3
    #     [2, 2, 2, 2, 2, 2, 2],  # 5 = Bunny 4
    #     [2, 2, 2, 2, 2, 2, 2]  # 6 = Bulkhead
    # ]
    graph = [
        [0, 2, 2, 2, 0, 7],  # 0 = Start
        [9, 0, 2, 2, -1, 4],  # 1 = Bunny 0
        [9, 3, 0, 2, 1, 10],  # 2 = Bunny 1
        [9, 3, 2, 0, 1, 5],  # 3 = Bunny 2
        [9, 3, 2, 4, 0, 5],  # 4 = Bunny 3
        [9, 3, 2, 2, 2, 0],  # 5 = Bulkhead
    ]
#     graph = [
#   [0, 2, 2, 2, -1],  # 0 = Start
#   [9, 0, 3, 3, -1],  # 1 = Bunny 0
#   [9, 3, 0, 3, -1],  # 2 = Bunny 1
#   [9, 3, 3, 0, -1],  # 3 = Bunny 2
#   [9, 3, 3, 3,  0],  # 4 = Bulkhead
# ]
#     graph = [
#         [0, 0, 0, 0, 0, 0, 1],  # 0 = Start
#         [0, 0, 0, 0, 0, 0, 1],  # 1 = Bunny 0
#         [0, 0, 0, 0, 0, 0, 1],  # 2 = Bunny 1
#         [0, 0, 0, 0, 0, 0, 1],  # 3 = Bunny 2
#         [0, 0, 0, 0, 0, 0, 1],  # 4 = Bunny 3
#         [0, 0, 0, 0, 0, 0, 0],  # 5 = Bunny 4
#         [0, 0, 0, 0, 0, 0, 0]  # 6 = Bulkhead
# ]
#     graph = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]

#     graph = [[0,0,1],
#             [0,0,1],
#             [0,0,1]]

    # graph = [
    #     [0, 2, 2, 2, 0, 5],  # 0 = Start
    #     [9, 0, 2, 2, -1, 4],  # 1 = Bunny 0
    #     [9, 3, 0, 2, 1, 10],  # 2 = Bunny 1
    #     [9, 3, 2, 0, 1, 5],  # 3 = Bunny 2
    #     [9, 3, 2, 4, 0, 5],  # 4 = Bunny 3
    #     [9, 3, 2, 2, 2, 0],  # 5 = Bulkhead
    # ]
    # size = random.randint(3,7)
    # print(size)
    # graph=[]
    # for i in range(size):
    #     temp = []
    #     for j in range(size):
    #        x temp.append(random.randint(-1,1000))
    #     graph.append(temp)
    #     print(temp)
    # pr = cProfile.Profile()
    # pr.enable()
    # time_limit = random.randint(0,1)
    # print(time_limit)
    print(answer(graph, 3))
    # pr.disable()
    # pr.print_stats(sort='time')

if __name__ == "__main__":
    main()