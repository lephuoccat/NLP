import numpy as np


class RNN:
    vertices = dict()
    edges = list()
    inp = ""
    output = ""
    memories = dict()
    node_values = dict()

    def __init__(self, rnn_spec):
        self.vertices = rnn_spec["vertices"]
        self.edges = rnn_spec["edges"]
        self.inp = rnn_spec["input"]
        self.outp = rnn_spec["output"]
        self.memories = rnn_spec["memories"]
        for i in self.memories:
            self.node_values[i] = np.zeros(self.vertices[i]["num_nodes"])

# assume edges in topological order
    def apply(self, observation):
        temp_out = np.empty([0, 0])
        for z in range(observation.shape[0]):
            self.node_values[self.inp] = observation[z]
            seen_targets = list()
            for i in range(len(self.edges)):
                if not self.edges[i]["target_id"] in seen_targets:
                    target = self.edges[i]["target_id"]
                    seen_targets.append(target)
                    source_ids = dict()
                    source_ids[self.edges[i]["source_id"]
                               ] = self.edges[i]["weights"]
                    for j in range(i+1, len(self.edges)):
                        if self.edges[j]["target_id"] == target:
                            source_ids[self.edges[j]["source_id"]
                                       ] = self.edges[j]["weights"]
                    # print("TARGET: ", target)
                    # print("SOURCE IDS: ", source_ids.keys())
                    x = list()
                    for k in source_ids.keys():
                        # print(k, self.node_values[k])
                        # print(k, source_ids[k])
                        x.append(np.dot(self.node_values[k], source_ids[k]))
         #           print ("sum", x)
                    x_sum = sum(x) + self.vertices[target]["bias"]
       #             print("X_SUM: ", x_sum)
                    self.node_values[target] = self.vertices[target]["activation"](
                        x_sum)
       #             print(self.node_values[target])
            temp_out = np.append(temp_out, self.node_values[self.outp])

            for i in (self.memories.keys()):
                self.node_values[i] = self.node_values[self.memories[i]]
        return temp_out

        # get the source_id of edge
        # get node value from node_values
        # multiply by weight
        # add bias
        # apply activation fn
        # add to node_values
