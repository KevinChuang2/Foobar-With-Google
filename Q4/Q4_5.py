
def answer(entrances, exits, path):
    graph = init_preflow(entrances, exits, path)
    # graph_status(graph)
    do_again = False
    curr =0
    while curr < len(graph):
        if graph[curr].inc_flow != 0 and curr != len(graph)-1 and curr !=0:
            graph[curr].push_relabel(graph)
            do_again = True
        if curr == len(graph) -1 and do_again:
            do_again = False
            curr = 0
        # graph_status(graph)
        curr +=1
    graph_status(graph)
    return graph[len(graph)-1].inc_flow

class Vertex:
    def __init__(self, vertex_num, edges_in, edges, path, height):
        self.num = vertex_num
        self.edges = edges
        self.edges_in = edges_in
        self.flow = [0 for x in range(0, len(self.edges))]
        if vertex_num != -1:
            self.capacities = [path[vertex_num][x] for x in self.edges]
        else:
            self.capacities = [sum(path[x]) for x in self.edges]
        self.inc_flow = 0
        self.height = height

    def push_relabel(self, graph):
        push = False
        for num, edge in enumerate(self.edges):
            if graph[edge+1].height < self.height:

                if sum([graph[edge+1].flow[x] - graph[edge+1].capacities[x] for x in range(0,len(graph[edge+1].flow))])!=0 or not graph[edge+1].flow:
                    temp = min(self.inc_flow, self.capacities[num]-self.flow[num])
                    if temp != 0:
                        push = True
                    self.flow[num]+=temp
                    self.inc_flow-=temp
                    graph[edge+1].inc_flow+=temp

        if not push:
            temp = self.height
            self.height = min(graph[edge+1].height for edge in self.edges_in+self.edges)+1
            if temp == self.height:
                edge = self.edges_in[min(self.edges_in)]

                graph[edge+1].inc_flow+=self.inc_flow
                # print(graph[edge+1].flow[(graph[edge+1].edges.index(self.num))])
                graph[edge + 1].flow[(graph[edge + 1].edges.index(self.num))]-=self.inc_flow
                self.inc_flow = 0

    def serialize(self):
        flow_capacities = [str(self.flow[x]) + '/' + str(self.capacities[x]) for x in range(0, len(self.flow))]
        return {
            "vertex_num": self.num,
            "edges incoming": self.edges_in,
            "edges": self.edges,
            "flow/capacities": flow_capacities,
            "incoming flow": self.inc_flow,
            "height": self.height
        }


def init_preflow(entrances, exits, path):
    residual_graph = []
    source = Vertex(-1, [], entrances, path, len(path) + 2)
    source.flow = [x for x in source.capacities]
    residual_graph.append(source)
    sink = Vertex(len(path),exits, [], path, 0)
    for room_num, ver in enumerate(path):
        temp_entr = []
        for index, num in enumerate(path[room_num]):
            if num != 0:
                temp_entr.append(index)
        new_vert = Vertex(room_num, [], temp_entr, path, 0)
        if room_num in entrances:
            # new_vert.flow = [x for x in new_vert.capacities]
            new_vert.inc_flow = source.flow[room_num]
        elif room_num in exits:
            new_vert.edges = [len(path)]
            new_vert.flow = [0]
            new_vert.capacities = [sum([path[x][room_num] for x in range(0, len(path))])]
        residual_graph.append(new_vert)
    residual_graph.append(sink)
    for vertex in residual_graph:
        if vertex.edges:
            for edge in vertex.edges:
                if not vertex.num in residual_graph[edge+1].edges_in:
                    residual_graph[edge+1].edges_in += [vertex.num]
    return residual_graph


def graph_status(graph):
    for vert in graph:
        print(vert.serialize())
    print('\n')


def main():
    # entrances = [0]
    # exits = [3]
    # path = [[0, 7, 0, 0], #entrance
    #         [0, 0, 6, 0],
    #         [0, 0, 0, 8],
    #         [9, 0, 0, 0]] #end
    entrances = [0, 1]
    exits = [4, 5]
    path = [
        [0, 0, 4, 6, 9, 9],  # Room 0: Bunnies
        [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
        [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
        [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
        [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
        [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
    ]
    print(answer(entrances, exits, path))


if __name__ == "__main__":
    main()
