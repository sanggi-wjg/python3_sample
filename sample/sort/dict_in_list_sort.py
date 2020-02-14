"""
https://inma.tistory.com/138
"""
sample = [
    { 'genre': 'classic', 'plays': 500, 'idx': 0 },
    { 'genre': 'pop', 'plays': 600, 'idx': 1 },
    { 'genre': 'classic', 'plays': 150, 'idx': 2 },
    { 'genre': 'classic', 'plays': 800, 'idx': 3 },
    { 'genre': 'pop', 'plays': 2500, 'idx': 4 }
]

sortSample = sorted(sample, key = lambda s: s['plays'], reverse = True)
print(sortSample)
