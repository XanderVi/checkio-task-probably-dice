"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

import random

TESTS = {
    "1. Basics": [
        {
            "input": [2, 6, 3],
            "answer": 0.05556,
            "show": 0.0556,
            "explanation": [0, 0, 50, 100, 150, 200, 250, 300, 250, 200, 150, 100, 50]
        },
        {
            "input": [2, 6, 4],
            "answer": 0.08333,
            "show": 0.0833,
            "explanation": [0, 0, 50, 100, 150, 200, 250, 300, 250, 200, 150, 100, 50]
        },
        {
            "input": [2, 6, 7],
            "answer": 0.16667,
            "show": 0.1667,
            "explanation": [0, 0, 50, 100, 150, 200, 250, 300, 250, 200, 150, 100, 50]
        },
        {
            "input": [2, 3, 5],
            "answer": 0.22222,
            "show": 0.2222,
            "explanation": [0, 0, 100, 200, 300, 200, 100]
        },
        {
            "input": [2, 3, 7],
            "answer": 0.0,
            "show": 0.0,
            "explanation": [0, 0, 100, 200, 300, 200, 100]
        },
        {
            "input": [3, 6, 7],
            "answer": 0.06944,
            "show": 0.0694,
            "explanation": [0, 0, 0, 11, 33, 67, 111, 167, 233, 278, 300, 300, 278, 233, 167, 111, 67, 33, 11]
        },
        {
            "input": [10, 10, 50],
            "answer": 0.03749,
            "show": 0.0375,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 4, 6,
                            9, 12, 16, 21, 27, 35, 44, 55, 67, 80, 96, 112, 130, 149, 169, 188, 208, 227, 244, 260, 274,
                            285, 293, 298, 300, 298, 293, 285, 274, 260, 244, 227, 208, 188, 169, 149, 130, 112, 96, 80,
                            67, 55, 44, 35, 27, 21, 16, 12, 9, 6, 4, 3, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0]
        },
    ],
    "2. Small": [
        {
            "input": [1, 2, 999],
            "answer": 0.0,
            "show": 0.0,
            "explanation": [0, 300, 300]
        },
        {
            "input": [1, 2, 0],
            "answer": 0.0,
            "show": 0.0,
            "explanation": [0, 300, 300]
        },
        {
            "input": [1, 2, 1],
            "answer": 0.5,
            "show": 0.5,
            "explanation": [0, 300, 300]
        },
        {
            "input": [1, 2, 2],
            "answer": 0.5,
            "show": 0.5,
            "explanation": [0, 300, 300]
        },
        {
            "input": [1, 2, 3],
            "answer": 0.0,
            "show": 0.0,
            "explanation": [0, 300, 300]
        },
        {
            "input": [2, 2, 1],
            "answer": 0.0,
            "show": 0.0,
            "explanation": [0, 0, 150, 300, 150]
        },
        {
            "input": [2, 2, 2],
            "answer": 0.25,
            "show": 0.25,
            "explanation": [0, 0, 150, 300, 150]
        },
        {
            "input": [2, 2, 3],
            "answer": 0.5,
            "show": 0.5,
            "explanation": [0, 0, 150, 300, 150]
        },
        {
            "input": [2, 2, 4],
            "answer": 0.25,
            "show": 0.25,
            "explanation": [0, 0, 150, 300, 150]
        },
        {
            "input": [2, 2, 5],
            "answer": 0.0,
            "show": 0.0,
            "explanation": [0, 0, 150, 300, 150]
        },
        {
            "input": [1, 8, 3],
            "answer": 0.125,
            "show": 0.125,
            "explanation": [0, 300, 300, 300, 300, 300, 300, 300, 300]
        },
    ],
    "Big": [
        {
            "input": [10, 20, 10],
            "answer": 0.0,
            "show": 0.0,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14,
                            16, 19, 22, 25, 28, 32, 36, 40, 45, 50, 55, 61, 67, 74, 81, 89, 96, 105, 113, 122, 131, 140,
                            150, 159, 169, 179, 189, 199, 208, 218, 227, 236, 245, 253, 260, 267, 274, 280, 285, 290,
                            293, 296, 298, 300, 300, 300, 298, 296, 293, 290, 285, 280, 274, 267, 260, 253, 245, 236,
                            227, 218, 208, 199, 189, 179, 169, 159, 150, 140, 131, 122, 113, 105, 96, 89, 81, 74, 67,
                            61, 55, 50, 45, 40, 36, 32, 28, 25, 22, 19, 16, 14, 12, 11, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1,
                            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]
        },
        {
            "input": [10, 20, 47],
            "answer": 0.0001,
            "show": 0.0001,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14,
                            16, 19, 22, 25, 28, 32, 36, 40, 45, 50, 55, 61, 67, 74, 81, 89, 96, 105, 113, 122, 131, 140,
                            150, 159, 169, 179, 189, 199, 208, 218, 227, 236, 245, 253, 260, 267, 274, 280, 285, 290,
                            293, 296, 298, 300, 300, 300, 298, 296, 293, 290, 285, 280, 274, 267, 260, 253, 245, 236,
                            227, 218, 208, 199, 189, 179, 169, 159, 150, 140, 131, 122, 113, 105, 96, 89, 81, 74, 67,
                            61, 55, 50, 45, 40, 36, 32, 28, 25, 22, 19, 16, 14, 12, 11, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1,
                            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]
        },
        {
            "input": [10, 20, 48],
            "answer": 0.00013,
            "show": 0.0001,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14,
                            16, 19, 22, 25, 28, 32, 36, 40, 45, 50, 55, 61, 67, 74, 81, 89, 96, 105, 113, 122, 131, 140,
                            150, 159, 169, 179, 189, 199, 208, 218, 227, 236, 245, 253, 260, 267, 274, 280, 285, 290,
                            293, 296, 298, 300, 300, 300, 298, 296, 293, 290, 285, 280, 274, 267, 260, 253, 245, 236,
                            227, 218, 208, 199, 189, 179, 169, 159, 150, 140, 131, 122, 113, 105, 96, 89, 81, 74, 67,
                            61, 55, 50, 45, 40, 36, 32, 28, 25, 22, 19, 16, 14, 12, 11, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1,
                            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]
        },
        {
            "input": [10, 20, 49],
            "answer": 0.00016,
            "show": 0.0002,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14,
                            16, 19, 22, 25, 28, 32, 36, 40, 45, 50, 55, 61, 67, 74, 81, 89, 96, 105, 113, 122, 131, 140,
                            150, 159, 169, 179, 189, 199, 208, 218, 227, 236, 245, 253, 260, 267, 274, 280, 285, 290,
                            293, 296, 298, 300, 300, 300, 298, 296, 293, 290, 285, 280, 274, 267, 260, 253, 245, 236,
                            227, 218, 208, 199, 189, 179, 169, 159, 150, 140, 131, 122, 113, 105, 96, 89, 81, 74, 67,
                            61, 55, 50, 45, 40, 36, 32, 28, 25, 22, 19, 16, 14, 12, 11, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1,
                            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]
        },
        {
            "input": [10, 20, 114],
            "answer": 0.01921,
            "show": 0.0192,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14,
                            16, 19, 22, 25, 28, 32, 36, 40, 45, 50, 55, 61, 67, 74, 81, 89, 96, 105, 113, 122, 131, 140,
                            150, 159, 169, 179, 189, 199, 208, 218, 227, 236, 245, 253, 260, 267, 274, 280, 285, 290,
                            293, 296, 298, 300, 300, 300, 298, 296, 293, 290, 285, 280, 274, 267, 260, 253, 245, 236,
                            227, 218, 208, 199, 189, 179, 169, 159, 150, 140, 131, 122, 113, 105, 96, 89, 81, 74, 67,
                            61, 55, 50, 45, 40, 36, 32, 28, 25, 22, 19, 16, 14, 12, 11, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1,
                            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]
        },
        {
            "input": [10, 20, 115],
            "answer": 0.0187,
            "show": 0.0187,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14,
                            16, 19, 22, 25, 28, 32, 36, 40, 45, 50, 55, 61, 67, 74, 81, 89, 96, 105, 113, 122, 131, 140,
                            150, 159, 169, 179, 189, 199, 208, 218, 227, 236, 245, 253, 260, 267, 274, 280, 285, 290,
                            293, 296, 298, 300, 300, 300, 298, 296, 293, 290, 285, 280, 274, 267, 260, 253, 245, 236,
                            227, 218, 208, 199, 189, 179, 169, 159, 150, 140, 131, 122, 113, 105, 96, 89, 81, 74, 67,
                            61, 55, 50, 45, 40, 36, 32, 28, 25, 22, 19, 16, 14, 12, 11, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1,
                            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]
        },
        {
            "input": [10, 20, 116],
            "answer": 0.01815,
            "show": 0.0181,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14,
                            16, 19, 22, 25, 28, 32, 36, 40, 45, 50, 55, 61, 67, 74, 81, 89, 96, 105, 113, 122, 131, 140,
                            150, 159, 169, 179, 189, 199, 208, 218, 227, 236, 245, 253, 260, 267, 274, 280, 285, 290,
                            293, 296, 298, 300, 300, 300, 298, 296, 293, 290, 285, 280, 274, 267, 260, 253, 245, 236,
                            227, 218, 208, 199, 189, 179, 169, 159, 150, 140, 131, 122, 113, 105, 96, 89, 81, 74, 67,
                            61, 55, 50, 45, 40, 36, 32, 28, 25, 22, 19, 16, 14, 12, 11, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1,
                            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]
        },
        {
            "input": [10, 20, 999],
            "answer": 0.0,
            "show": 0.0,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14,
                            16, 19, 22, 25, 28, 32, 36, 40, 45, 50, 55, 61, 67, 74, 81, 89, 96, 105, 113, 122, 131, 140,
                            150, 159, 169, 179, 189, 199, 208, 218, 227, 236, 245, 253, 260, 267, 274, 280, 285, 290,
                            293, 296, 298, 300, 300, 300, 298, 296, 293, 290, 285, 280, 274, 267, 260, 253, 245, 236,
                            227, 218, 208, 199, 189, 179, 169, 159, 150, 140, 131, 122, 113, 105, 96, 89, 81, 74, 67,
                            61, 55, 50, 45, 40, 36, 32, 28, 25, 22, 19, 16, 14, 12, 11, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1,
                            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]
        },
        {
            "input": [10, 20, 201],
            "answer": 0.0,
            "show": 0.0,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14,
                            16, 19, 22, 25, 28, 32, 36, 40, 45, 50, 55, 61, 67, 74, 81, 89, 96, 105, 113, 122, 131, 140,
                            150, 159, 169, 179, 189, 199, 208, 218, 227, 236, 245, 253, 260, 267, 274, 280, 285, 290,
                            293, 296, 298, 300, 300, 300, 298, 296, 293, 290, 285, 280, 274, 267, 260, 253, 245, 236,
                            227, 218, 208, 199, 189, 179, 169, 159, 150, 140, 131, 122, 113, 105, 96, 89, 81, 74, 67,
                            61, 55, 50, 45, 40, 36, 32, 28, 25, 22, 19, 16, 14, 12, 11, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1,
                            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]
        },
        {
            "input": [9, 19, 47],
            "answer": 0.00075,
            "show": 0.0008,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 7, 8, 9, 11, 13, 16, 18, 21, 24, 28, 32, 37, 42,
                            47, 53, 60, 67, 74, 82, 90, 99, 108, 118, 128, 138, 149, 159, 170, 181, 192, 203, 213, 224,
                            234, 243, 252, 261, 268, 276, 282, 287, 292, 295, 298, 299, 300, 299, 298, 295, 292, 287,
                            282, 276, 268, 261, 252, 243, 234, 224, 213, 203, 192, 181, 170, 159, 149, 138, 128, 118,
                            108, 99, 90, 82, 74, 67, 60, 53, 47, 42, 37, 32, 28, 24, 21, 18, 16, 13, 11, 9, 8, 7, 5, 4,
                            4, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0]
        },
        {
            "input": [9, 19, 48],
            "answer": 0.00089,
            "show": 0.0009,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 7, 8, 9, 11, 13, 16, 18, 21, 24, 28, 32, 37, 42,
                            47, 53, 60, 67, 74, 82, 90, 99, 108, 118, 128, 138, 149, 159, 170, 181, 192, 203, 213, 224,
                            234, 243, 252, 261, 268, 276, 282, 287, 292, 295, 298, 299, 300, 299, 298, 295, 292, 287,
                            282, 276, 268, 261, 252, 243, 234, 224, 213, 203, 192, 181, 170, 159, 149, 138, 128, 118,
                            108, 99, 90, 82, 74, 67, 60, 53, 47, 42, 37, 32, 28, 24, 21, 18, 16, 13, 11, 9, 8, 7, 5, 4,
                            4, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0]
        },
        {
            "input": [9, 19, 89],
            "answer": 0.02384,
            "show": 0.0238,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 7, 8, 9, 11, 13, 16, 18, 21, 24, 28, 32, 37, 42,
                            47, 53, 60, 67, 74, 82, 90, 99, 108, 118, 128, 138, 149, 159, 170, 181, 192, 203, 213, 224,
                            234, 243, 252, 261, 268, 276, 282, 287, 292, 295, 298, 299, 300, 299, 298, 295, 292, 287,
                            282, 276, 268, 261, 252, 243, 234, 224, 213, 203, 192, 181, 170, 159, 149, 138, 128, 118,
                            108, 99, 90, 82, 74, 67, 60, 53, 47, 42, 37, 32, 28, 24, 21, 18, 16, 13, 11, 9, 8, 7, 5, 4,
                            4, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0]
        },
        {
            "input": [9, 19, 90],
            "answer": 0.02387,
            "show": 0.0239,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 7, 8, 9, 11, 13, 16, 18, 21, 24, 28, 32, 37, 42,
                            47, 53, 60, 67, 74, 82, 90, 99, 108, 118, 128, 138, 149, 159, 170, 181, 192, 203, 213, 224,
                            234, 243, 252, 261, 268, 276, 282, 287, 292, 295, 298, 299, 300, 299, 298, 295, 292, 287,
                            282, 276, 268, 261, 252, 243, 234, 224, 213, 203, 192, 181, 170, 159, 149, 138, 128, 118,
                            108, 99, 90, 82, 74, 67, 60, 53, 47, 42, 37, 32, 28, 24, 21, 18, 16, 13, 11, 9, 8, 7, 5, 4,
                            4, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0]
        },
        {
            "input": [9, 19, 91],
            "answer": 0.02384,
            "show": 0.0238,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 7, 8, 9, 11, 13, 16, 18, 21, 24, 28, 32, 37, 42,
                            47, 53, 60, 67, 74, 82, 90, 99, 108, 118, 128, 138, 149, 159, 170, 181, 192, 203, 213, 224,
                            234, 243, 252, 261, 268, 276, 282, 287, 292, 295, 298, 299, 300, 299, 298, 295, 292, 287,
                            282, 276, 268, 261, 252, 243, 234, 224, 213, 203, 192, 181, 170, 159, 149, 138, 128, 118,
                            108, 99, 90, 82, 74, 67, 60, 53, 47, 42, 37, 32, 28, 24, 21, 18, 16, 13, 11, 9, 8, 7, 5, 4,
                            4, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0]
        },
        {
            "input": [9, 19, 141],
            "answer": 0.00015,
            "show": 0.0001,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 7, 8, 9, 11, 13, 16, 18, 21, 24, 28, 32, 37, 42,
                            47, 53, 60, 67, 74, 82, 90, 99, 108, 118, 128, 138, 149, 159, 170, 181, 192, 203, 213, 224,
                            234, 243, 252, 261, 268, 276, 282, 287, 292, 295, 298, 299, 300, 299, 298, 295, 292, 287,
                            282, 276, 268, 261, 252, 243, 234, 224, 213, 203, 192, 181, 170, 159, 149, 138, 128, 118,
                            108, 99, 90, 82, 74, 67, 60, 53, 47, 42, 37, 32, 28, 24, 21, 18, 16, 13, 11, 9, 8, 7, 5, 4,
                            4, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0]
        },
        {
            "input": [9, 19, 142],
            "answer": 0.00012,
            "show": 0.0001,
            "explanation": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 7, 8, 9, 11, 13, 16, 18, 21, 24, 28, 32, 37, 42,
                            47, 53, 60, 67, 74, 82, 90, 99, 108, 118, 128, 138, 149, 159, 170, 181, 192, 203, 213, 224,
                            234, 243, 252, 261, 268, 276, 282, 287, 292, 295, 298, 299, 300, 299, 298, 295, 292, 287,
                            282, 276, 268, 261, 252, 243, 234, 224, 213, 203, 192, 181, 170, 159, 149, 138, 128, 118,
                            108, 99, 90, 82, 74, 67, 60, 53, 47, 42, 37, 32, 28, 24, 21, 18, 16, 13, 11, 9, 8, 7, 5, 4,
                            4, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0]
        },
    ]
}
