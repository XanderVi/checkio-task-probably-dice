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
    "Basics": [],
    "Small": [],
    "Big": []
}

def addTest(c, i, a):
    TESTS[c].append({"input": i, "answer": a})

addTest("Basics", [2, 6, 3], 0.05556)
addTest("Basics", [2, 6, 4], 0.08333)
addTest("Basics", [2, 6, 7], 0.16667)
addTest("Basics", [2, 3, 5], 0.22222)
addTest("Basics", [2, 3, 7], 0.00000)
addTest("Basics", [3, 6, 7], 0.06944)
addTest("Basics", [10, 10, 50], 0.03749)

addTest("Small", [1, 2, 999], 0.00000)
addTest("Small", [1, 2, 0], 0.00000)
addTest("Small", [1, 2, 1], 0.50000)
addTest("Small", [1, 2, 2], 0.50000)
addTest("Small", [1, 2, 3], 0.00000)
addTest("Small", [2, 2, 1], 0.00000)
addTest("Small", [2, 2, 2], 0.25000)
addTest("Small", [2, 2, 3], 0.50000)
addTest("Small", [2, 2, 4], 0.25000)
addTest("Small", [2, 2, 5], 0.00000)
addTest("Small", [1, 8, 3], 0.12500)

addTest("Big", [10, 20, 10], 0.00000) # Too small to display with only 4 digits, but not actually 0
addTest("Big", [10, 20, 47], 0.00010)
addTest("Big", [10, 20, 48], 0.00013)
addTest("Big", [10, 20, 49], 0.00016)
addTest("Big", [10, 20, 114], 0.01921)
addTest("Big", [10, 20, 115], 0.01870)
addTest("Big", [10, 20, 116], 0.01815)
addTest("Big", [10, 20, 999], 0.0000)
addTest("Big", [10, 20, 201], 0.0000)
addTest("Big", [9, 19, 47], 0.00075)
addTest("Big", [9, 19, 48], 0.00089)
addTest("Big", [9, 19, 89], 0.02384)
addTest("Big", [9, 19, 90], 0.02387)
addTest("Big", [9, 19, 91], 0.02384)
addTest("Big", [9, 19, 141], 0.00015)
addTest("Big", [9, 19, 142], 0.00012)
