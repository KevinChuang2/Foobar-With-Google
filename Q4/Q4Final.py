def answer(times, time_limit):
    shortest_graph = []
    lengths = bford(0, times)
    # check for negative cycles with just one iteration of bellman-ford
    if lengths == 'Negative Cycle':
        # return all bunnies because if there's a neg cycle, we can get to any bunny
        answer = []
        for i in range(0, len(times) - 2):
            answer.append(i)
        return answer
    #construct graph of shortest paths using bellman-ford on every vertex. This gets rid of any cycles that would happen.
    #For example, let's say that we wanted to go from 0->2->0->3->0->4 and this is our best path.
    #Bellman ford on every vertex would shift the values such that the value for going from 2 -> 3 is the
    #same as the value it takes to go from 2->0->3. This means that we never have to check for a vertex that we have
    #already visited. If it visits a different node to go to like 2->1->3, 2 to 1 would be visited because we haven't
    #visited the 1st bunny yet.
    for x in range(0, len(times)):
        lengths = bford(x, times)
        shortest_graph.append(lengths)
    times = shortest_graph
    queue = []
    smallest = times[0][0]
    # find smallest of entire array
    for temp, x in enumerate(times):
        for count, y in enumerate(x):
            if y < smallest:
                smallest = y
    #starting from the start, add all possible paths from the start
    #queue[0] has the path, queue[1] has the time left
    for x in range(1, len(times)):
        queue.append([[0, x], time_limit - times[0][x]])
    #sort the queue based on which path has the most amount of time left. Unnecessary but speeds it up
    queue.sort(key=lambda x: x[1], reverse=True)
    finished = []

    while queue:
        #this is the node that we are on
        last_node = queue[0][0][-1]
        #how much time we have left
        last_time = queue[0][1]
        #this is the move we are going to check
        added_move = queue[0]
        #if we are at the bulkhead
        if last_node == len(times) - 1:
            #and we have more than or have 0 time (we can escape!)
            if added_move[1] >= 0:
                #add this to our list of routes that are possible.
                finished.append(added_move)
                #if we have found that we can visit every bunny and escape, just quit because we found it.
                if len(set(added_move[0])) == len(times):
                    break
        #going through every path from the last node
        for x in range(0, len(times)):
            #can't visit the same node we are on
            if x == last_node:
                pass
            #because of bellman ford on the whole graph, we don't need to visit a vertex we have already seen.
            #our paths are guaranteed to be the fastest with no cycles.
            elif x in added_move[0]:
                pass
            else:
                #we can't add added_move we have to make another list
                temp = [[], 0]
                #add our path up until now
                for i in added_move[0]:
                    temp[0].append(i)
                #add the node we last visited
                temp[0].append(x)
                #adjust time based on the distance
                temp[1] = last_time - times[last_node][x]
                #if our time is smaller than the smallest number in array, impossible to get to bulkhead so stop
                if temp[1] < smallest:
                    continue
                #else insert to front of queue (we delete queue[0] so we insert it into position 1)
                else:
                    queue.insert(1, temp)
        del (queue[0])
    #we are done with looking through paths
    #sort our list of finished paths by the longest paths first
    finished.sort(key=lambda x: len(x[0]), reverse=True)
    #max is the most amount of bunnies we can get
    if finished:
        max = len(finished[0][0])
    else:
        return []
    best_moves = []
    for move in finished:
        #if the path has the same amount as the max
        if len(move[0]) == max:
            #use the set to order it and remove the start and bulkhead
            set_temp = set(move[0])
            set_temp.remove(0)
            set_temp.remove(len(times) - 1)
            best_moves.append(set_temp)
        else:
            break
    #this will order it by the lowest indices of bunnies we can make
    best_moves.sort(key=lambda x: sum(x))
    #first one is guaranteed to be the best move
    list_of_bunnies = list(best_moves[0])
    #readjust number of bunnies because position 1 is the 0th bunny
    for x in range(0, len(list_of_bunnies)):
        list_of_bunnies[x] -= 1
    return list_of_bunnies

#implementation of bellman ford algorithm (well known)
#takes a source vertex and finds the shortest length to every vertex in graph.
def bford(source, graph):
    distance = []
    for x in range(0, len(graph)):
        distance.append(float('inf'))
    distance[source] = 0
    for i in range(0, len(graph) - 1):
        for vertex_num, vertex in enumerate(graph):
            for target, edge in enumerate(vertex):
                if distance[vertex_num] + graph[vertex_num][target] < distance[target]:
                    distance[target] = distance[vertex_num] + graph[vertex_num][target]
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
    print(answer(graph, 10))
    # pr.disable()
    # pr.print_stats(sort='time')

if __name__ == "__main__":
    main()