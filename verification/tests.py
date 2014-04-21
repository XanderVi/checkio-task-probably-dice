"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [3, 3, 3, 3, 6, 6],
            "answer": True
        },
        {
            "input": [4, 4, 4, 4, 4, 4],
            "answer": True
        }
        {
            "input": [1, 1, 1, 4],
            "answer": True
        }
        {
            "input": [1, 2, 3, 4, 5, 6],
            "answer": False
        }
    ],
    "Small": [
        {
            "input": [1, 1, 1],
            "answer": False
        },
        {
            "input": [1, 1, 2],
            "answer": False
        },
        {
            "input": [1, 1, 3],
            "answer": True
        },
        {
            "input": [2, 2, 2],
            "answer": False
        },
        {
            "input": [3, 3, 3],
            "answer": True
        },
        {
            "input": [4, 4, 4],
            "answer": True
        }
    ]
    "Big": [
        {
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "answer": False
        },
        {
            "input": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            "answer": False
        },
        {
            "input": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
            "answer": True
        },
        {
            "input": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            "answer": True
        },
        {
            "input": [1, 5, 5, 5, 5, 6, 6, 6, 6, 10],
            "answer": True
        },
        {
            "input": [2, 4, 6, 8, 10, 12, 14, 16, 18],
            "answer": False
        }
    ]
}
