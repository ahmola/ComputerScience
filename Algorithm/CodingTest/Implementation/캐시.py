import sys

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    cities = [c.lower() for c in cities]
    cache = []
    time = 0

    for city in cities:
        if city not in cache:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city)
            time += 5
        else:
            if len(cache) > 1:
                index = cache.index(city)
                cache.append(cache.pop(index))
            time += 1
    return time

cachesize = int(sys.stdin.readline().strip())
cities = list(sys.stdin.readline().split())
print(solution(cachesize, cities))