def solution(nums):
    pokemon = {}
    for n in nums:
        if n in pokemon:
            pokemon[n] += 1
        else:
            pokemon[n] = 1

    if len(pokemon) > len(nums)//2:
        return len(nums)//2

    return len(pokemon)

print(solution([3,3,3,2,2,4]))