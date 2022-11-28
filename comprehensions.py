# set comprehensions

l = [10, 20, 3, 4, 10, 20, 7, 3]
set1 = {x for x in l if x % 2 == 0}  # {10,20,4} Note: no repeats
set2 = {x for x in l if x % 2 != 1}  # {3,7} Note: you can't control order


# dictionary comprehensions
l1 = [1, 3, 4, 2, 5]
dictionary1 = {x: x**3 for x in l1}  # creating dictionary from list


d2 = {x: f"ID{x}" for x in range(5)}

l2 = [101, 103, 102]
l3 = ["next", "gen", "courses"]
d3 = {l2[i]: l3[i] for i in range(len(l2))}
# should use zib tho


# inverting dictionaries
d1 = {101: "gfg", 103: "practice", 102: "ide"}
d2 = {v: k for (k, v) in d1.items()}
