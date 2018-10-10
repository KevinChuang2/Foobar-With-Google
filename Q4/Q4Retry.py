from copy import copy, deepcopy
import random
import cProfile
import math
def answer(times, time_limit):

    answer = []
    # print('Times original:')
    # for x in range(0, len(times)):
    #     print(times[x])
    shortest_graph = []
    # print('Graph after bford:')
    lengths = bford(0, times)
    # print(lengths)
    # check for negative cycles
    if lengths == 'Negative Cycle':
        # return all bunnies because if there's a neg cycle, we can get to any bunny
        for i in range(0, len(times) - 2):
            answer.append(i)
        return answer
    # construct graph of shortest paths using bford on each vertice. This speeds
    # up the search
    for x in range(0, len(times)):
        lengths = bford(x, times)
        print(lengths)
        shortest_graph.append(lengths)
    times = shortest_graph
    queue = []
    smallest = times[0][0]
    # print(len(times[0])-1)
    bulk_cost = times[0][len(times[0]) - 1]

    # find smallest of entire array
    # bulk cost checks before hand to make sure its possible to even get to the bulk cost
    # gets rid of case where it loops adding nothing to the time forever
    smallest_nums = [float('inf')] * (len(times[0]) - 1)
    # print(smallest_nums)
    for temp, x in enumerate(times):
        for count, y in enumerate(x):
            if count == len(times[0]) - 1:
                if bulk_cost > y and temp != len(times[0]) - 1:
                    bulk_cost = y
            if y < smallest:
                smallest = y
            if times[temp][count] < smallest_nums[count - 1] and temp != count and count != 0:
                smallest_nums[count - 1] = times[temp][count]
    # if sum(smallest_nums) > time_limit:
    #     return []
    # print(f'bulk cost is {bulk_cost}')
    while sum(smallest_nums) > time_limit:
        smallest_nums.remove(max(smallest_nums))
    possible_length = len(smallest_nums)
    # print(possible_length)
    if bulk_cost > time_limit:
        return []
    if smallest > time_limit:
        return []
    # print(f'smallest is {smallest}')
    # append all nodes out of the start to the queue
    for x in range(1, len(times)):
        queue.append([[0, x], time_limit - times[0][x]])
    queue.sort(key=lambda x: x[1], reverse=True)
    #print(f'queue is {queue}')
    finished = []
    counter = 0
    # print(queue)

    while queue:
        # print(f'queue is {queue}')
        # print(f'finished is {finished}')
        # print(f'queue len is {len(queue)}')
        counter += 1
        if counter > math.factorial(possible_length+1):
            break
        # print(f'counter is {counter}')
        last_node = queue[0][0][-1]
        last_time = queue[0][1]
        # print(f'last node is {last_node}')
        added_move = queue[0]
        # print(f'added move is {added_move}')
        # print(f'count is {added_move[0].count(x)}')
        if last_node == len(times) - 1:
            if added_move[1] >= 0:
                finished.append(added_move)
                if len(set(added_move[0])) > possible_length + 1:
                    break
        for x in range(0, len(times)):
            if x == last_node:
                pass
            elif added_move[0].count(x) > len(times) - 1:
                break
            else:
                # print(f'added move is {added_move}')
                temp = [[], 0]
                for i in added_move[0]:
                    temp[0].append(i)
                temp[0].append(x)
                temp[1] = last_time - times[last_node][x]

                if temp[1] < smallest:
                    continue
                else:
                    # if queue:
                    #     if len(set(queue[0][0]))<len(set(temp[0])):
                    #         queue.insert(1,temp)
                    #     else:
                    #         queue.append(temp)
                    if len(temp[0]) > 2:
                        # print(f'temp is {temp}')
                        last_occurence = len(temp[0][::-1][1:]) - 1 - temp[0][::-1][1:].index(x) if x in temp[0][
                                                                                                         ::-1][
                                                                                                         1:] else -1
                        # print(f'last occ: {last_occurence}')
                        # print(f'x is {x}')
                        if last_occurence == -1:
                            # print(f'inserted {temp} early')
                            queue.insert(1, temp)
                            continue
                        elif last_occurence == 0:
                            queue.append(temp)
                        if temp[0][-2] != temp[0][last_occurence - 1]:
                            queue.append(temp)
        del (queue[0])

    finished.sort(key=lambda x: len(set(x[0])), reverse=True)
    # print(finished)
    if finished:
        max_set = len(set(finished[0][0]))
    else:
        return []
    best_moves = []
    best_times = []
    for move in finished:
        if len(set(move[0])) == max_set:
            print(move[0])
            set_temp = set(move[0])
            set_temp.remove(0)
            set_temp.remove(len(times) - 1)
            best_moves.append(set_temp)
            best_times.append(move[1])
    best_moves.sort(key=lambda x: sum(x))
    list_of_bunnies = list(best_moves[0])
    for x in range(0, len(list_of_bunnies)):
        list_of_bunnies[x] -= 1
    return list_of_bunnies

def main():
    # graph = [
    #     [0, 1, 5, 3, 1, 6, 3],  # 0 = Start
    #     [9, 0, 2, 2, 1, 2, 1],  # 1 = Bunny 0
    #     [9, 3, 0, 2, 1, 6, 5],  # 2 = Bunny 1
    #     [9, 3, 2, 0, 1, 1, 32],  # 3 = Bunny 2
    #     [9, 7, 1, 2, 0, 1, 2],  # 4 = Bunny 3
    #     [9, 0, 1, 3, 1, 0, 2],  # 5 = Bunny 4
    #     [9, 3, 2, 2, 0, 3, 0],  # 6 = Bulkhead
    # ]
    #     graph = [
    #   [0, 0, 0, 0, 0, 0, 0],  # 0 = Start
    #         [0, 0, 0, 0, 0, 0, 0],  # 1 = Bunny 0
    #         [0, 0, 0, 0, 0, 0, 0],  # 2 = Bunny 1
    #         [0, 0, 0, 0, 0, 0, 0],  # 3 = Bunny 2
    #                 [0, 0, 0, 0, 0, 0, 0],  # 4 = Bunny 3
    #         [0, 0, 0, 0, 0, 0, 0],  # 5 = Bunny 4
    #         [0, 0, 0, 0, 0, 0, 0]  # 6 = Bulkhead
    # ]
    # graph = [
    #   [0, 2, 2, 2, -1],  # 0 = Start
    #   [9, 0, 2, 2, -1],  # 1 = Bunny 0
    #   [9, 3, 0, 2, -1],  # 2 = Bunny 1
    #   [9, 3, 2, 0, -1],  # 3 = Bunny 2
    #   [9, 3, 2, 2,  0],  # 4 = Bulkhead
    # ]
    graph = [
        [0, 2, 2, 2, 2, 2, 2],  # 0 = Start
        [0, 2, 2, 2, 2, 2, 2],  # 1 = Bunny 0
        [0, 2, 2, 2, 2, 2, 2],  # 2 = Bunny 1
        [0, 2, 2, 2, 2, 2, 2],  # 3 = Bunny 2
        [0, 2, 2, 2, 2, 2, 2],  # 4 = Bunny 3
        [0, 2, 2, 2, 2, 2, 2],  # 5 = Bunny 4
        [0, 2, 2, 2, 2, 2, 2]  # 6 = Bulkhead
    ]
    size = random.randint(3,7)
    print(size)
    # graph=[]
    # for i in range(size):
    #     temp = []
    #     for j in range(size):
    #         temp.append(random.randint(-20,100))
    #     graph.append(temp)
    #     print(temp)
    pr = cProfile.Profile()
    pr.enable()
    time_limit = random.randint(0,50)
    print(time_limit)
    # graph = [[38, -7, -8, -20, 95, 76],
    #         [84, 16, 1, -6, 17, 29],
    #         [34, 3, 98, 91, 98, 78],
    #         [97, 80, 63, 20, 47, 33],
    #         [36, 50, 0, 51, 19, 30],
    #         [14, -2, 74, 49, 88, 21]]
    print(answer(graph,11))

def bford(source, graph):
    distance = []
    # pred = []
    for x in range(0, len(graph)):
        distance.append(float('inf'))
        # pred.append(0)
    distance[source] = 0
    # print(source)
    # print(graph)
    # print(f'distance is {distance}')
    # print(f'pred is {pred}')
    for i in range(0, len(graph) - 1):
        for vertex_num, vertex in enumerate(graph):
            for target, edge in enumerate(vertex):
                if distance[vertex_num] + graph[vertex_num][target] < distance[target]:
                    distance[target] = distance[vertex_num] + graph[vertex_num][target]
                    # pred[target] = vertex_num
    # print(f'distance is {distance}')
    # print(f'pred is {pred}')
    for vertex_num, vertex in enumerate(graph):
        for target, edge in enumerate(vertex):
            if distance[vertex_num] + graph[vertex_num][target] < distance[target]:
                return 'Negative Cycle'
    return distance

if __name__ == "__main__":
    main()