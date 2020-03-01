import numpy as np
spec = {
    "vertices": {
        "h1": {
            # logistic func
            "activation": lambda x: 1/(1+np.exp(-x)),
            "num_nodes": 5
        },
        "h2": {
            # linear func
            "activation": lambda x: x,
            "num_nodes": 9
        },
        "input": {
            "activation": None,
            "num_node": 1e5
        },
        "memory1": {
            "activation": lambda x: x,
            "num_node": 30
        },
        "outpu1": {
            "activation": lambda x: x,
            "num_node": 65
        }
    },
    "edges": [
        {
            "source_id": "memory0",
            "target_id": "h1"
        },
        {
            "source_id": "input",
            "target_id": "h1"
        },
        {
            "source_id": "h1",
            "target_id": "h2"
        },
        {
            "source_id": "h1",
            "target_id": "memory1"
        },
        {
            "source_id": "h2",
            "target_id": "output1"
        }
    ],
    "input": [
        "input"
    ],
    "output": [
        "output1"
    ],
    "memory_in": [
        "memory0"
    ],
    "memory_out": [
        "memory1"
    ],
}