def solution(tickets):
    tickets.sort()
    used = [False] * len(tickets)
    result = []

    def dfs(start, path):
        if len(path) == len(tickets) + 1:
            result.append(path)
            return True

        for i in range(len(tickets)):
            if not used[i] and tickets[i][0] == start:
                used[i] = True
                if dfs(tickets[i][1], [tickets[i][1]]):
                    return True
                used[i] = False
        return False

    dfs("ICN", ["ICN"])

    return result

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))