import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def dfs(s):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs(s)
            s.pop()

dfs([])