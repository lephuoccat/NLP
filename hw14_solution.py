import numpy as np
import math

spec = {
    "vertices": {
        "input": {
            "num_nodes": 13,
            "activation": lambda x: x,
            "bias": 0
        },
        "memory_in0": {
            "num_nodes": 3,
            "activation": lambda x: x,
            "bias": 0
        },
        "mul": {
            "num_nodes": 1,
            "activation": lambda x: 0 if x[0]<0 else (x[0]+1)*x[1],
            "bias": 0
        },
        "hold": {
            "num_nodes": 1,
            "activation": lambda x: x[1] + x[0] if x[1] > 0 and x[0] > 0 else x[0] if x[0] == -1 and x[1] != 0 else x[1],
            "bias": 0
        },
        "memory_out0": {
            "num_nodes": 3,
            "activation": lambda x: x,
            "bias": 0
        },
        "output": {
            "num_nodes": 1,
            "activation": lambda x: x,
            "bias": 0
        }
    },
    "edges": [
        {
            "source_id": "input",
            "target_id": "mul",
            "weights": np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 1], [0, 1], [0, -1], [0, -1], [0, -1]])
        },
        {
            "source_id": "memory_in0",
            "target_id": "mul",
            "weights": np.array([[1, 0], [0, 0], [0, 0]])
        },
        {
            "source_id": "input",
            "target_id": "hold",
            "weights": np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, -1], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])
        },
        {
            "source_id": "memory_in0",
            "target_id": "hold",
            "weights": np.array([[1, 0], [0, 0], [0, 0]])
        },
        {
            "source_id": "hold",
            "target_id": "memory_out0",
            "weights": np.array([1, 0, 0])
        },
        {
            "source_id": "mul",
            "target_id": "output",
            "weights":  np.array([1])
        }
    ],
    "input": "input",
    "output": "output",
    "memories": {
        "memory_in0": "memory_out0",
    }
}
