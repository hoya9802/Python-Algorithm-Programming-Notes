# DP
def solution(x, y, n):
    INF = int(1e9)
    answer = [INF] * (y+1)
    answer[x]=0
    for i in range(x+1, y+1):
        if answer[i-n] >= 0:
            answer[i] = min(answer[i], answer[i-n] + 1)
        if i % 2 == 0 and answer[i//2] >= 0:
            answer[i] = min(answer[i], answer[i//2] + 1)
        if i % 3 == 0 and answer[i//3] >= 0:
            answer[i] = min(answer[i], answer[i//3] + 1)
    if answer[-1] == INF:
        return -1
    return answer[-1]

# bfs
def solution(x, y, n):
    answer = set()
    answer.add(x)
    ans = 0
    while answer:
        if y in answer:
            return ans
        
        tmp = set()
        for i in answer:
            if i + n <= y:
                tmp.add(i+n)
            if i * 2 <= y:
                tmp.add(2*i)
            if i * 3 <= y:
                tmp.add(3*i)
        answer = tmp
        ans += 1

    
    return -1