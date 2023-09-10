import random

def generate_random_frozenset():
    random_set = set()
    while len(random_set) < 30:
        random_set.add(random.randint(1, 100))
    return frozenset(random_set)

frozensets = [generate_random_frozenset() for _ in range(10)]
soma_frozensets = {frozenset: sum(frozenset) for frozenset in frozensets}

for i, (frozenset, soma) in enumerate(soma_frozensets.items(), start=1):
    print(f"Frozenset {i}: {frozenset} - Soma: {soma}")
