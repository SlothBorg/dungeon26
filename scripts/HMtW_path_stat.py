from itertools import combinations_with_replacement

numbers = [1, 2, 3, 4]
target = 10
count = 4

results = [
    combo
    for combo in combinations_with_replacement(numbers, count)
    if sum(combo) == target
]

print(f"Found {len(results)} combinations:\n")
for combo in results:
    print(combo)
